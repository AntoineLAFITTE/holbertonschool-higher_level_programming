#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class defines a square with a private instance attribute: size.
    Size validation is performed to ensure it is a positive integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with size validation.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private attribute

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The current square area (size * size).
        """
        return self.__size ** 2
