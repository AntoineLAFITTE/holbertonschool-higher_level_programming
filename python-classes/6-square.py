#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    This class defines a square with a private
    instance attributes: size and position.
    Size validation is performed to ensure it is a positive integer.
    Position validation ensures it is a tuple of two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with size and position validation.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size  # Use the setter for validation
        self.position = position  # Use the setter for validation

    @property
    def size(self):
        """
        Getter for the private attribute size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private attribute size with validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for the private attribute position.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the private attribute position with validation.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The current square area (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # to stdout,
        respecting the position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            # Print the vertical space
            for _ in range(self.__position[1]):
                print("")

            # Print the square with leading spaces for horizontal position
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
