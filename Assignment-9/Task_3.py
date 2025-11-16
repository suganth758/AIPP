"""
Calculator Module
=================

This module provides basic arithmetic operations including addition,
subtraction, multiplication, and division. Each function demonstrates
NumPy-style docstrings and serves as an example of combining manually
written documentation with AI-assisted docstrings.
"""

def add(a: float | int, b: float | int) -> float | int:
    """
    Add two numbers.

    Parameters
    ----------
    a : float or int
        The first number to add.
    b : float or int
        The second number to add.

    Returns
    -------
    float or int
        The sum of the two numbers.

    Notes
    -----
    This docstring was generated using AI assistance.
    """
    return a + b


def subtract(a: float | int, b: float | int) -> float | int:
    """
    Subtract one number from another.

    Parameters
    ----------
    a : float or int
        The number from which another will be subtracted.
    b : float or int
        The number to subtract.

    Returns
    -------
    float or int
        The result of the subtraction.

    Notes
    -----
    This docstring was generated using AI assistance.
    """
    return a - b


def multiply(a: float | int, b: float | int) -> float | int:
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float or int
        First number in the multiplication.
    b : float or int
        Second number in the multiplication.

    Returns
    -------
    float or int
        Product of `a` and `b`.

    Notes
    -----
    This docstring was manually written.
    """
    return a * b


def divide(a: float | int, b: float | int) -> float | int:
    """
    Divide one number by another.

    Parameters
    ----------
    a : float or int
        The numerator.
    b : float or int
        The denominator.

    Returns
    -------
    float or int
        Result of the division.

    Raises
    ------
    ZeroDivisionError
        If `b` is zero.

    Notes
    -----
    This docstring was manually written.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

# --- Example Usage and Output ---
print("--- Calculator Module Examples ---")

# Addition
result_add = add(10, 5)
print(f"10 + 5 = {result_add}")

# Subtraction
result_subtract = subtract(10, 5)
print(f"10 - 5 = {result_subtract}")

# Multiplication
result_multiply = multiply(10, 5)
print(f"10 * 5 = {result_multiply}")

# Division
result_divide = divide(10, 5)
print(f"10 / 5 = {result_divide}")

# Division by zero (demonstrating error handling)
try:
    result_zero_divide = divide(10, 0)
    print(f"10 / 0 = {result_zero_divide}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
