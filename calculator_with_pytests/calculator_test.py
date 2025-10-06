# Pytests to test the individual instance methods of the Calculator class.
import pytest 
from calculator import Calculator

# Test for the add function
def test_add():
    calc = Calculator(2, 3, "+")
    assert calc.add() == 5

# Test for the subtract function    
def test_subtract():
    calc = Calculator(4, 1, "-")
    assert calc.subtract() == 3

# Test for the multiply   
def test_multiply():
    calc = Calculator(5, 3, "*")
    assert calc.multiply() == 15
    
# Test for the divide
def test_divide():
    calc = Calculator(6, 2, "/")
    assert calc.divide() == 3
    calc = Calculator(6, 0, "/")
    try:
        calc.divide()
    except ZeroDivisionError as e:
        assert str(e) == "Cannot divide by zero."
    