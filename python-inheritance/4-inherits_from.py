#!/usr/bin/python3
"""This module defines a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from the specified class,
but is not an instance of the class itself.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class,
    but is not an instance of the class itself.

    Args:
        obj: The object to check.
        a_class: The class to match against the type or inheritance of obj.

    Returns:
        bool: True if obj is an instance of a class that inherited from
        a_class,
        but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
