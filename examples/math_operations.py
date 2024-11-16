"""
math_operations.py

This module provides basic mathematical operations with detailed explanations.
It includes functions for addition, subtraction, multiplication, and division.

Functions:
    add(a, b): Returns the sum of a and b.
    subtract(a, b): Returns the difference between a and b.
    multiply(a, b): Returns the product of a and b.
    divide(a, b): Returns the quotient of a divided by b.

Examples:
    >>> from math_operations import add, subtract
    >>> add(5, 3)
    8
    >>> subtract(10, 4)
    6
"""

def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The sum of a and b.

    Example:
        >>> add(2, 3)
        5
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference between two numbers.

    Parameters:
        a (float or int): The number to subtract from.
        b (float or int): The number to subtract.

    Returns:
        float or int: The difference between a and b.

    Example:
        >>> subtract(5, 3)
        2
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two numbers.

    Parameters:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        float or int: The product of a and b.

    Example:
        >>> multiply(4, 5)
        20
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a divided by b.

    Parameters:
        a (float or int): The numerator.
        b (float or int): The denominator. Must not be zero.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If b is zero.

    Example:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("The denominator cannot be zero.")
    return a / b
