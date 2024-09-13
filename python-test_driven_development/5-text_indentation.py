#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The input text (must be a string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".:?":
            result += "\n\n"
            i += 1
            # Skip les whitespace après punctuation
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # .strip to print wihtout unnecessary spaces
    print(result.strip(), end="")
