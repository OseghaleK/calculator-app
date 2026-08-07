"""The raw math. Nothing in here knows anything about the user."""


def addition(a, b):
    """Return a plus b."""
    return a + b


def subtraction(a, b):
    """Return b subtracted from a."""
    return a - b


def multiplication(a, b):
    """Return a times b."""
    return a * b


def division(a, b):
    """Return a divided by b, refusing a zero divisor.

    This is the LBYL half of the error handling. Python would raise on
    its own, but checking first means the message the user sees is one
    I wrote rather than a raw interpreter error.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
