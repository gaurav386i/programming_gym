"""
Interview Prompt
Design a control plane component that safely attaches and detaches 
storage volumes to VMs while handling partial failures and retries.

Requirements:
+ It will  attach storage volumes to VMs 
+ It will detach storag volumes from VMs
+ Should handle partial failure like if storage attach/detach failed midway 
+ Vm can have multiple valumes attached 
+ It should retry if failed to attach for a given number of retries .
+ desired state eventually matches actual state
+ Operations are idempotent / duplicate requests are safe 
+ partial failure are recoverable


Entities:
VolumeAttachmentController

VM

Volume

VolumeAttachment

Relationships in Entities: 
VolumeAttachmentController > has > VM and volume 
VM >> has single or multiple vol attachments

VolumeAttachmentController:
- Available Volumes: 
- VMs

 + attach_volume(vm_id, vol_id)
 + detach_volume(vm_id, vol_id)

VM:
- vm_id: str
- volumes: list


VolumeRecord:
- vol_id: str
- desired_vm_id: str
- observed_vm_id: str

- state: Enum
- retrycount: int 


"""

from enum import Enum
from dataclasses import dataclass, field
from threading import Lock
from typing import Optional


class VolumeState(Enum):
    # Transitional
    ATTACHING = "attaching"
    DETACHING = "detaching"

    # Stable
    ATTACHED = "attached"
    DETACHED = "detached"

    # Failure
    ERROR = "error"


MAX_RETRIES = 3


@dataclass
class VM:
    vm_id: str

    # vol_id -> VolumeRecord
    attached_volumes: dict[str, "VolumeRecord"] = field(default_factory=dict)


@dataclass
class VolumeRecord:
    vol_id: str

    # User intent
    desired_vm_id: Optional[str] = None

    # Actual infra state
    observed_vm_id: Optional[str] = None

    state: VolumeState = VolumeState.DETACHED

    retry_count: int = 0

    last_error: Optional[str] = None


class VolumeAttachmentController:

    def __init__(self):
        self._vms: dict[str, VM] = {}

        self._volumes: dict[str, VolumeRecord] = {}

        self._lock = Lock()

    # ==========================================================
    # Registration Helpers
    # ==========================================================

    def register_vm(self, vm: VM):
        self._vms[vm.vm_id] = vm

    def register_volume(self, volume: VolumeRecord):
        self._volumes[volume.vol_id] = volume

    # ==========================================================
    # Desired State APIs
    # ==========================================================

    def request_attach(self, vm_id: str, vol_id: str):

        volume = self._volumes[vol_id]

        # Desired state change only
        volume.desired_vm_id = vm_id

    def request_detach(self, vol_id: str):

        volume = self._volumes[vol_id]

        # Desired detach
        volume.desired_vm_id = None

    # ==========================================================
    # Reconciliation Loop
    # ==========================================================

    def reconcile(self, vol_id: str):

        with self._lock:

            volume = self._volumes[vol_id]

            # Retry guard
            if volume.retry_count >= MAX_RETRIES:
                volume.state = VolumeState.ERROR
                return

            # --------------------------------------------------
            # ATTACH FLOW
            # --------------------------------------------------

            if volume.desired_vm_id is not None:

                # Idempotent success
                if (
                    volume.observed_vm_id == volume.desired_vm_id
                    and volume.state == VolumeState.ATTACHED
                ):
                    return

                # Prevent multi-attach corruption
                if (
                    volume.observed_vm_id is not None
                    and volume.observed_vm_id != volume.desired_vm_id
                ):
                    volume.retry_count += 1
                    volume.last_error = "Volume attached to another VM"
                    return

                # Transitional state
                volume.state = VolumeState.ATTACHING

                try:
                    # Simulated infra attach operation

                    vm = self._vms[volume.desired_vm_id]

                    vm.attached_volumes[volume.vol_id] = volume

                    # Persist observed state AFTER success
                    volume.observed_vm_id = vm.vm_id

                    volume.state = VolumeState.ATTACHED

                    volume.retry_count = 0

                    volume.last_error = None

                except Exception as e:
                    volume.retry_count += 1
                    volume.last_error = str(e)

            # --------------------------------------------------
            # DETACH FLOW
            # --------------------------------------------------

            else:

                # Already detached
                if (
                    volume.observed_vm_id is None
                    and volume.state == VolumeState.DETACHED
                ):
                    return

                volume.state = VolumeState.DETACHING

                try:

                    old_vm = self._vms.get(volume.observed_vm_id)

                    if old_vm:
                        old_vm.attached_volumes.pop(volume.vol_id, None)

                    volume.observed_vm_id = None

                    volume.state = VolumeState.DETACHED

                    volume.retry_count = 0

                    volume.last_error = None

                except Exception as e:
                    volume.retry_count += 1
                    volume.last_error = str(e)
        
                
