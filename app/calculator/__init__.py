"""The REPL. This is the only part of the app that talks to the user."""

from app.calculation import CalculationFactory

WELCOME = "Calculator ready. Type 'help' for commands or 'exit' to quit."

# Built from the factory's registry so adding an operation never means
# remembering to update this string too.
MENU = (
    "Operations: " + ", ".join(CalculationFactory.available()) + "\n"
    "Commands: help, history, exit"
)


def parse_number(value):
    """Turn user text into a float, or raise with a readable message.

    This is the EAFP half of the error handling. There is no reliable
    way to look at a string and know it will convert cleanly, so the
    conversion is attempted and the failure is handled afterward.
    """
    try:
        return float(value)
    except ValueError as error:
        raise ValueError(f"'{value}' is not a valid number.") from error


def show_history(history):
    """Print the calculations recorded so far this session."""
    if not history:
        print("No calculations yet.")
        return
    for position, entry in enumerate(history, start=1):
        print(f"{position}. {entry}")


def run():
    """Read, evaluate, print, loop until the user types exit."""
    history = []
    print(WELCOME)

    while True:
        command = input("Command: ").strip().lower()

        if command == "exit":
            print("Goodbye.")
            break

        if command == "help":
            print(MENU)
            continue

        if command == "history":
            show_history(history)
            continue

        # Check the command before asking for numbers. Otherwise someone
        # who typos the operation gets asked for two numbers first and
        # only then told it was wrong.
        if command not in CalculationFactory.available():
            print(f"Unknown command '{command}'. Type 'help' for options.")
            continue

        try:
            a = parse_number(input("First number: "))
            b = parse_number(input("Second number: "))
            calculation = CalculationFactory.create(command, a, b)
            result = calculation.execute()
        except ValueError as error:
            print(f"Invalid input: {error}")
            continue
        except ZeroDivisionError as error:
            print(f"Math error: {error}")
            continue

        history.append(calculation.describe(result))
        print(f"Result: {result}")
