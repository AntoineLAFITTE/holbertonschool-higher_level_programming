#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # 1 Validate and initialize width
        self.integer_validator("width", width)
        self.__width = width

        # 2Validate and initialize height
        self.integer_validator("height", height)
        self.__height = height
