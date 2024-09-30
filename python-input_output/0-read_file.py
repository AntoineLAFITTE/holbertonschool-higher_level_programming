#!/usr/bin/python3
"""module including read_file method"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints the text file to stdout.

    Args:
        filename (str): file to read.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
