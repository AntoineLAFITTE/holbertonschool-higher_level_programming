#!/usr/bin/env/python3
from abc import ABC, abstractmethod
import math
"""This module defines shapes and demonstrates duck typing
for shape information
"""


class Shape(ABC):
    """Abstract base class representing a geometric shape

    Subclasses must implement area and perimeter methods
    """

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of a shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of a shape"""
        pass


class Circle(Shape):
    """This subclass represents a circle

    Atributes:
        radius (float): The radius of the circle
        """

    def __init__(self, radius):
        """Initializes the Circle with a radius"""
        self.radius = radius

    def area(self):
        """Calculates the area of a circle using formula πr².

        Returns:
            float: The area of the circle
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates the perimeter pf the circle using the formula 2πr.

        Returns:
            float: The perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """This subclass represents a rectangle

    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    """

    def __init__(self, width, height):
        """Initializes the Rectangle with a width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculates area of the rectangle using the formula width * height

        Returns:
            float: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle using the
        formula 2 * (width + height)

        Returns:
            float: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing

    Args:
        shape: An object expected to have area and perimeter methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
