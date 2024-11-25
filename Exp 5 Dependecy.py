
from dependency_injector import containers, providers

# Step 1: Define the operations
class Adder:
    def calculate(self, a: float, b: float) -> float:
        return a + b

class Subtractor:
    def calculate(self, a: float, b: float) -> float:
        return a - b

# Step 2: Define the Calculator
class Calculator:
    def __init__(self, operation):
        self.operation = operation  # Injected dependency

    def execute(self, a: float, b: float) -> float:
        return self.operation.calculate(a, b)

# Step 3: Create a container for dependency injection
class Container(containers.DeclarativeContainer):
    adder = providers.Factory(Adder)          # Factory to create Adder
    subtractor = providers.Factory(Subtractor) # Factory to create Subtractor

    calculator = providers.Factory(           # Factory for Calculator
        Calculator, 
        operation=adder  # Default is Adder
    )

# Step 4: Use the container
if __name__ == "__main__":
    container = Container()  # Initialize the container

    # Perform addition
    adder_calculator = container.calculator()  # Default uses Adder
    print("Addition Result:", adder_calculator.execute(10, 5))  # Output: 15

    # Perform subtraction
    container.calculator.override(
        providers.Factory(Calculator, operation=container.subtractor)
    )
    subtractor_calculator = container.calculator()
    print("Subtraction Result:", subtractor_calculator.execute(10, 5))  # Output: 5
  