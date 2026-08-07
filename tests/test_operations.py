"""Tests for the arithmetic functions.

Values here use halves and quarters on purpose. Decimals like 0.1 do not
compare exactly in floating point, so a test written with them fails for
reasons that have nothing to do with the math being wrong.
"""

import pytest

from app.operation import addition, subtraction, multiplication, division


@pytest.mark.parametrize(
    "operation, a, b, expected",
    [
        (addition, 187.5, 12.5, 200.0),
        (addition, 42, 18, 60),
        (addition, -25, 25, 0),
        (subtraction, 187.5, 143.25, 44.25),
        (subtraction, 60, 75, -15),
        (subtraction, 0, 30, -30),
        (multiplication, 143.25, 4, 573.0),
        (multiplication, 15, 8, 120),
        (multiplication, 27, 0, 0),
        (division, 573.0, 4, 143.25),
        (division, 120, 8, 15),
        (division, 45, 2, 22.5),
    ],
)
def test_operations_return_expected(operation, a, b, expected):
    assert operation(a, b) == expected


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        division(45, 0)
