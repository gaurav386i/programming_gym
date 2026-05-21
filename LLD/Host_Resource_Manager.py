"""
Requirements Capabilities : 
1. ResourceManager , can reserve capacity , assign capacity 
2. CPU , Memory . 
3. Capacity 
4. handle request :  provisioning request , release request 
5. VM or Container 
6 . provisioning requested will specify what we are going to provisioning VM or Container .

Entities : 
ResourceManager Request Capacity Instance (VM, Container) 
ResourceManager >> handle >> 
Request Resourcemanager >> will have >> Capacity
"""
import threading
import uuid

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class InstanceType(Enum):
    VM = "VM"
    CONTAINER = "Container"


@dataclass
class Capacity:
    cpu: float
    memory: float

    def __add__(self, other: "Capacity"):
        return Capacity(
            self.cpu + other.cpu,
            self.memory + other.memory
        )

    def __sub__(self, other: "Capacity"):
        return Capacity(
            self.cpu - other.cpu,
            self.memory - other.memory
        )

    def __le__(self, other: "Capacity"):
        return (
            self.cpu <= other.cpu and
            self.memory <= other.memory
        )


@dataclass
class Instance:
    id: str
    capacity: Capacity
    type: InstanceType


class VM(Instance):
    def __init__(self, id: str, capacity: Capacity):
        super().__init__(id, capacity, InstanceType.VM)


class Container(Instance):
    def __init__(self, id: str, capacity: Capacity):
        super().__init__(id, capacity, InstanceType.CONTAINER)


class Request(ABC):

    @abstractmethod
    def execute(self, manager: "ResourceManager"):
        pass


@dataclass
class ProvisioningRequest(Request):
    instance_type: InstanceType
    capacity: Capacity

    def execute(self, manager: "ResourceManager"):
        return manager.provision(
            self.instance_type,
            self.capacity
        )


@dataclass
class ReleaseRequest(Request):
    instance_id: str

    def execute(self, manager: "ResourceManager"):
        return manager.release(self.instance_id)


class ResourceManager:

    def __init__(self, total_capacity: Capacity):

        self.total_capacity = total_capacity

        self.available_capacity = Capacity(
            total_capacity.cpu,
            total_capacity.memory
        )

        self.used_capacity = Capacity(0.0, 0.0)

        self.instances: dict[str, Instance] = {}

        # minimal thread safety
        self.lock = threading.RLock()

    def handle_request(self, request: Request):
        return request.execute(self)

    def get_available_capacity(self):

        # optional lock for consistent read
        with self.lock:
            return Capacity(
                self.available_capacity.cpu,
                self.available_capacity.memory
            )

    def _reserve_capacity(self, reservation: Capacity):

        # caller already holds lock

        if reservation <= self.available_capacity:

            self.available_capacity = (
                self.available_capacity - reservation
            )

            self.used_capacity = (
                self.used_capacity + reservation
            )

            return True

        return False

    def provision(
        self,
        instance_type: InstanceType,
        capacity: Capacity
    ):

        with self.lock:

            if not self._reserve_capacity(capacity):

                print(
                    "Instance provisioning failed. "
                    "Capacity not available"
                )

                return None

            instance_id = str(uuid.uuid4())[:8]

            if instance_type == InstanceType.VM:

                instance = VM(
                    instance_id,
                    capacity
                )

            else:

                instance = Container(
                    instance_id,
                    capacity
                )

            self.instances[instance_id] = instance

            print(
                f"Instance {instance_id} created successfully "
                f"with cpu={capacity.cpu} "
                f"mem={capacity.memory}"
            )

            return instance_id

    def release(self, instance_id: str):

        with self.lock:

            if instance_id not in self.instances:

                print(
                    f"Instance with id "
                    f"{instance_id} not found"
                )

                return False

            instance = self.instances.pop(instance_id)

            self.used_capacity = (
                self.used_capacity - instance.capacity
            )

            self.available_capacity = (
                self.available_capacity + instance.capacity
            )

            print(
                f"Released instance "
                f"{instance.type.value} [{instance_id}]"
            )

            return True