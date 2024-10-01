#!/usr/bin/python3
"""Module containing the load_from_json_file function"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON string.

    Returns:
        object: The Python object deserialized from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
