#!/usr/bin/python3
"""
This module provides a function that add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number to add (must be a int or float).
        b: The second number to add (must be a int or float, defaults to 98).

    Returns:
        The sum of the two numbers after casting them to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
