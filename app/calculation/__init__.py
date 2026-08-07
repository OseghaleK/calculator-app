"""Calculation classes and the factory that builds them."""

from app.operation import addition, subtraction, multiplication, division


class CalculationFactory:
    """Creates calculation objects from a registered operation name."""

    _registry = {}

    @classmethod
    def register(cls, name):
        """Decorator that adds a calculation class to the registry."""

        def wrapper(calculation_class):
            cls._registry[name] = calculation_class
            return calculation_class

        return wrapper

    @classmethod
    def available(cls):
        """Return the registered operation names in alphabetical order."""
        return sorted(cls._registry)

    @classmethod
    def create(cls, name, a, b):
        """Build a calculation, or raise if the name is not registered.

        LBYL again. Checking the registry first means an unsupported
        name produces my message rather than a KeyError.
        """
        if name not in cls._registry:
            raise ValueError(f"Unsupported operation: '{name}'.")
        return cls._registry[name](a, b)


class Calculation:
    """Base class holding two operands and producing a result."""

    symbol = "?"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        """Subclasses supply the actual arithmetic."""
        raise NotImplementedError("Subclasses must implement execute.")

    def describe(self, result):
        """Return a readable record of this calculation for the history."""
        return f"{self.a} {self.symbol} {self.b} = {result}"


@CalculationFactory.register("add")
class Addition(Calculation):
    """Adds two numbers."""

    symbol = "+"

    def execute(self):
        return addition(self.a, self.b)


@CalculationFactory.register("subtract")
class Subtraction(Calculation):
    """Subtracts the second number from the first."""

    symbol = "-"

    def execute(self):
        return subtraction(self.a, self.b)


@CalculationFactory.register("multiply")
class Multiplication(Calculation):
    """Multiplies two numbers."""

    symbol = "*"

    def execute(self):
        return multiplication(self.a, self.b)


@CalculationFactory.register("divide")
class Division(Calculation):
    """Divides the first number by the second."""

    symbol = "/"

    def execute(self):
        return division(self.a, self.b)
