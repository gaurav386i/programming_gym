from abc import ABC, abstractmethod


class Operation:
    
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

class Addition(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b
      

class Substraction(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b
     
class Multiplication(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b
     
class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        return a / b
     

class OperationsFactory:
    def __init__(self):
        self.operations = {
            "+": Addition,
            "-": Substraction,
            "*": Multiplication,
            "/": Division
        }
    
    def add_operation(self, operator: str, operation: Operation) -> None:
        if operator not in self.operations:
            self.operations[operator] = operation
        else:
            raise ValueError("Operation already exists")
    
    def get_operation(self, operator: str) -> Operation:
        operation_class = self.operations.get(operator)
        if not operation_class:
            raise ValueError("Operation not supporeted")
        return operation_class()


class Calculator:
    def __init__(self, factory: OperationsFactory):
        self.factory = factory

    def calculate(self, operator: str, a: float, b: float) -> float:
        operation = self.factory.get_operation(operator)

        return operation.execute(a, b)

factory = OperationsFactory()


class Modulus(Operation):
    def execute(self, a: float, b: float) -> float:
        return a % b


factory.add_operation("%", Modulus)

calc = Calculator(factory)


def test_calculator():

    assert calc.calculate("+", 4, 5) == 9

    assert calc.calculate("%", 5, 2) == 1
    

if __name__ == "__main__":
    test_calculator()




