# Command-Line Calculator

By Oseghale Akhimien

This is a calculator you run in the terminal. It keeps asking for input
until you tell it to stop, so you can do one calculation after another
without restarting it. It handles addition, subtraction, multiplication,
and division, and it tells you what went wrong instead of crashing when
you type something it does not expect.

## What you need

Python 3.11 or newer.

## Getting it running

Clone the repo and go into the folder.

    git clone git@github.com:OseghaleK/calculator-app.git
    cd calculator-app

Make a virtual environment and turn it on.

    python -m venv venv
    source venv/Scripts/activate

On macOS or Linux the second line is source venv/bin/activate instead.

Install what it needs.

    pip install -r requirements.txt

## Using it

Start it up.

    python -m app.calculator

It will ask for an operation. Type add, subtract, multiply, or divide,
and it will then ask you for two numbers. It prints the answer and comes
right back to the prompt for the next one.

Type help if you forget the options, and type exit when you are done.

Here is what a session looks like.

    Calculator ready. Type 'help' for options or 'exit' to quit.
    Operation: add
    First number: 12
    Second number: 8
    Result: 20.0
    Operation: exit
    Goodbye.

## When something goes wrong

If you type letters where a number should go, it says the input was not
a valid number and sends you back to the prompt. Your session keeps
going, nothing is lost.

If you try to divide by zero, it tells you that is not allowed instead
of throwing a Python error at you.

If you type an operation it does not recognize, it says so and reminds
you to type help.

## Running the tests

    pytest -v

The tests are in the tests folder, split between the arithmetic
functions and the loop itself. The project is set up to fail the test
run if coverage drops below 100 percent, so a passing run means every
line of the app was actually exercised.

## Automated testing

GitHub Actions runs the same test command every time anything is pushed
to main. If a test fails, or if coverage comes in under 100 percent, the
build fails and shows up red on the repository.