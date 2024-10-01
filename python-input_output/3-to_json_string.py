#!/usr/bin/python3
"""Module containing the to_json_string function"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (object): The object to be serialized into a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
