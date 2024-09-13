#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (must be int or float).

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
                   If each row of the matrix is not the same size.
                   If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists)of integers/floats"
        )

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError(
            "matrix must be a matrix (list of lists)of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # round with 2 decimal.
    return [[round(el / div, 2) for el in row] for row in matrix]
