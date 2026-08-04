import pytest

from main import add, divide, multiply, subtract, validate_numeric_inputs


def test_add_returns_sum_for_numbers():
    assert add(2, 3) == 5
    assert add(2.5, 3.5) == 6.0


def test_subtract_returns_difference():
    assert subtract(10, 4) == 6
    assert subtract(5.5, 2.5) == 3.0


def test_multiply_returns_product():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide_returns_quotient():
    assert divide(20, 4) == 5
    assert divide(7, 2) == 3.5


def test_divide_raises_for_zero_divisor():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_validate_numeric_inputs_accepts_numeric_strings():
    assert validate_numeric_inputs("2", "3.5") == [2.0, 3.5]


def test_validate_numeric_inputs_rejects_non_numeric_values():
    with pytest.raises(TypeError, match="Inputs must be numeric"):
        validate_numeric_inputs("two", 3)
