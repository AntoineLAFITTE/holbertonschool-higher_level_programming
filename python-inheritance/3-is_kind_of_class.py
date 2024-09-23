#!/usr/bin/python3
"""This module defines a function that checks if an object is an instance of,
or an instance of a class that inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of, or if obj is an instance of a
    class that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match the type or inheritance of obj.

    Returns:
        bool: True if obj is an instance or
        an instance of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
