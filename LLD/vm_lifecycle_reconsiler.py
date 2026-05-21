"""
Interviewer prompt: Design a control plane component that safely transitions a VM to its desired
state (e.g., Running, Stopped, Deleted) while handling partial failures.

++++

There should be a VMReconsiler that will transition VM to its desired state .
There should be VM with states .
There should be VMLifecycleState 
There should be VMOperations 

Does Reconsiler need to validate intent, 
Actions should be idempotent 
There are steady state and transitioning states

Entities: 

VMReconsiler (Orchestrator)
VMRecord  hold > (desired_state, observed_state)
LifecycleState (enum)
Actions (enum)


Class modeling 

VMReconsiler
- VMs 
+ reconsile >> contains reconcilation_logic reconsile(vm_record)

VMRecord
- vm_id
- disk_attached boolean
- desired_state
- obsered_state


scope: 
reconcilation_logic 
vm_record 
state 
actions

out of scope 
actual host actions 
api 
network calls
"""
import threading

from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class VMState(Enum):

    REQUESTED = "requested"
    PROVISIONING = "provisioning"
    STARTING = "starting"
    STOPPING = "stopping"
    DELETING = "deleting"

    RUNNING = "running"
    STOPPED = "stopped"
    DELETED = "deleted"

    ERROR = "error"


class VMAction(Enum):

    PROVISION_DISK = "provision_disk"
    START_VM = "start_vm"
    STOP_VM = "stop_vm"
    DELETE_VM = "delete_vm"

    WAIT = "wait"
    RETRY = "retry"
    NO_OP = "no_op"


@dataclass
class VMRecord:

    vm_id: str

    desired_state: VMState
    observed_state: VMState

    disk_attached: bool = False

    retry_count: int = 0
    last_error: Optional[str] = None

    # per-VM lock
    lock: threading.RLock = field(
        default_factory=threading.RLock,
        init=False,
        repr=False
    )


class VMReconciler:

    MAX_RETRIES = 3

    def reconcile(self, vm: VMRecord) -> VMAction:

        # lock only this VM
        with vm.lock:

            return self._reconcile_internal(vm)

    def _reconcile_internal(
        self,
        vm: VMRecord
    ) -> VMAction:

        # -----------------------------------------
        # Failure handling
        # -----------------------------------------
        if vm.retry_count >= self.MAX_RETRIES:

            print(
                f"[{vm.vm_id}] "
                f"max retries exceeded"
            )

            return VMAction.NO_OP

        # -----------------------------------------
        # Desired == Observed
        # -----------------------------------------
        if vm.desired_state == vm.observed_state:
            return VMAction.NO_OP

        # -----------------------------------------
        # Desired RUNNING
        # -----------------------------------------
        if vm.desired_state == VMState.RUNNING:
            return self._reconcile_running(vm)

        # -----------------------------------------
        # Desired STOPPED
        # -----------------------------------------
        if vm.desired_state == VMState.STOPPED:
            return self._reconcile_stopped(vm)

        # -----------------------------------------
        # Desired DELETED
        # -----------------------------------------
        if vm.desired_state == VMState.DELETED:
            return self._reconcile_deleted(vm)

        return VMAction.NO_OP

    # =================================================
    # RUNNING FLOW
    # =================================================

    def _reconcile_running(
        self,
        vm: VMRecord
    ) -> VMAction:

        if not vm.disk_attached:
            return VMAction.PROVISION_DISK

        if vm.observed_state in (
            VMState.REQUESTED,
            VMState.PROVISIONING,
            VMState.STOPPED,
            VMState.STARTING,
        ):
            return VMAction.START_VM

        if vm.observed_state == VMState.RUNNING:
            return VMAction.NO_OP

        return VMAction.WAIT

    # =================================================
    # STOPPED FLOW
    # =================================================

    def _reconcile_stopped(
        self,
        vm: VMRecord
    ) -> VMAction:

        if vm.observed_state in (
            VMState.RUNNING,
            VMState.STARTING,
        ):
            return VMAction.STOP_VM

        if vm.observed_state == VMState.STOPPED:
            return VMAction.NO_OP

        return VMAction.WAIT

    # =================================================
    # DELETE FLOW
    # =================================================

    def _reconcile_deleted(
        self,
        vm: VMRecord
    ) -> VMAction:

        if vm.observed_state in (
            VMState.RUNNING,
            VMState.STARTING,
        ):
            return VMAction.STOP_VM

        if vm.observed_state in (
            VMState.STOPPED,
            VMState.REQUESTED,
            VMState.PROVISIONING,
            VMState.DELETING,
        ):
            return VMAction.DELETE_VM

        if vm.observed_state == VMState.DELETED:
            return VMAction.NO_OP

        return VMAction.WAIT



