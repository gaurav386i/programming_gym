"""
Questions:  design a vending machine 


Requirements : 
What are prime capabilities of vending machine 
e.g it let user insert a coin, select product and dispence
Does it need to main and transition state like product 
selected to dispencing 
how many state this machine can have e.g NoCoin , HasCoin etc ...
I am asuuming three state for now NoCoin, HasCoin , Dispense 

error handling :
what to do if an user try to perform an invalid action e.g try to insert coin on a dispending 
machine 

In scope and Out of scope 
single coin , single product , three states , state transition . Exception handling 
for invalid actions 

Out of scope :
multi coin , multi product 

Entities 
VendingMachine
- initial_machine state
+ insert_coin()
+ select_product()
+ dispense

MachineState abstraction
+ insert_coin()
+ select_product()
+ dispense()
NoCoinState
HasCoinState
DispenseState

Relationship VendingMachine >> MachineState

states transitions looks like : NoCoinState >> HasCoinState >> DispenseState >> NoCoinState

"""
from abc import ABC, abstractmethod


class MachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine: "VendingMachine"):
        pass

    @abstractmethod
    def select_product(self, machine: "VendingMachine"):
        pass

    @abstractmethod
    def dispense(self, machine: "VendingMachine"):
        pass


class NoCoinState(MachineState):
    def insert_coin(self, machine: "VendingMachine"):
        print("Coin inserted select product")
        machine.set_state(HasCoinState())
    
    def select_product(self, machine: "VendingMachine"):
        print("Insert coin please")

    def dispense(self, machine: "VendingMachine"):
        print("Insert coin please")


class HasCoinState(MachineState):
    def insert_coin(self, machine: "VendingMachine"):
        print("Coin already inserted select product")
       
    
    def select_product(self, machine: "VendingMachine"):
        print("Product selected dispensing")
        machine.set_state(DispenseState())

    def dispense(self, machine: "VendingMachine"):
        print("Select product please")


class DispenseState(MachineState):
    def insert_coin(self, machine: "VendingMachine"):
        print("Please wait dispensing ....")
       
    
    def select_product(self, machine: "VendingMachine"):
        print("Please wait dispensing ....")
        

    def dispense(self, machine: "VendingMachine"):
        print("Please wait dispending ...")
        machine.set_state(NoCoinState())



class VendingMachine(MachineState):
    def __init__(self):
        self.current_state: MachineState = NoCoinState()

    def insert_coin(self) -> None:
        self.current_state.insert_coin(self)
    
    def select_product(self) -> None:
        self.current_state.select_product(self)

    def dispense(self) -> None:
       self.current_state.dispense(self)
    
    def set_state(self, state: MachineState) -> None:
        self.current_state = state


vending_machine = VendingMachine()

vending_machine.insert_coin()
vending_machine.select_product()
vending_machine.dispense()

