"""
test_calculator.py
------------------

Unit tests for calculator.py module using PyTest.
"""

import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Test addition function."""
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test subtraction function."""
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5
    assert subtract(0, 0) == 0


def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    """Test division function."""
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3

    # Test division by zero error
    with pytest.raises(ValueError):
        divide(5, 0)
