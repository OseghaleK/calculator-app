"""Tests for the calculation classes and the factory that creates them."""

import pytest

from app.calculation import (
    Calculation,
    Addition,
    Subtraction,
    Multiplication,
    Division,
    CalculationFactory,
)


@pytest.mark.parametrize(
    "name, expected_class",
    [
        ("add", Addition),
        ("subtract", Subtraction),
        ("multiply", Multiplication),
        ("divide", Division),
    ],
)
def test_factory_creates_correct_class(name, expected_class):
    assert isinstance(CalculationFactory.create(name, 1, 1), expected_class)


@pytest.mark.parametrize(
    "name, a, b, expected",
    [
        ("add", 187.5, 12.5, 200.0),
        ("subtract", 187.5, 143.25, 44.25),
        ("multiply", 15, 8, 120),
        ("divide", 120, 8, 15),
        ("divide", 45, 2, 22.5),
        ("add", -25, -25, -50),
    ],
)
def test_calculations_execute(name, a, b, expected):
    assert CalculationFactory.create(name, a, b).execute() == expected


def test_factory_rejects_unknown_operation():
    with pytest.raises(ValueError, match="Unsupported operation"):
        CalculationFactory.create("modulo", 45, 2)


def test_factory_lists_available_operations():
    assert CalculationFactory.available() == [
        "add",
        "divide",
        "multiply",
        "subtract",
    ]


def test_base_calculation_requires_execute():
    with pytest.raises(NotImplementedError):
        Calculation(1, 2).execute()


def test_describe_formats_the_record():
    assert Addition(187.5, 12.5).describe(200.0) == "187.5 + 12.5 = 200.0"


def test_division_by_zero_propagates():
    with pytest.raises(ZeroDivisionError):
        CalculationFactory.create("divide", 45, 0).execute()
