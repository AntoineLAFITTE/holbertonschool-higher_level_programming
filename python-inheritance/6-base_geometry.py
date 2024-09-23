#!/usr/bin/python3
"""This module defines a class BaseGeometry with an area method
that raises an exception."""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
