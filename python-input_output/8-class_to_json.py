#!/usr/bin/python3
"""Module containing the class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: The dictionary representation of the object's attributes.
    """
    return obj.__dict__
