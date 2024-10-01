#!/usr/bin/python3
"""Module containing the save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to be serialized and written to the file.
        filename (str): The name of the file where the JSON representation
        will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
