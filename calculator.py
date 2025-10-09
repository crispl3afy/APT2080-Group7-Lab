"""
calculator.py
--------------

A simple calculator module that performs basic arithmetic operations.
This module demonstrates clean code practices with proper docstrings and comments.

Author: Zawadi
Date: October 2025
"""

def add(a, b):
    """
    Adds two numbers together.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts one number from another.

    Args:
        a (float): The first number.
        b (float): The number to subtract from a.

    Returns:
        float: The difference between a and b.
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Divides one number by another.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Example inline comment:
# The following code only runs if the file is executed directly (not imported).
if _name_ == "_main_":
    print("Addition: ", add(10, 5))
    print("Subtraction: ", subtract(10, 5))
    print("Multiplication: ", multiply(10, 5))
    print("Division: ", divide(10, 5))
