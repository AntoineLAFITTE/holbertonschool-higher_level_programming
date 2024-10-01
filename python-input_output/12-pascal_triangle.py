#!/usr/bin/python3
"""Module containing the pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle.

    Args:
        n (int): The number of rows of Pascal’s triangle to generate.

    Returns:
        list: A list of lists where each inner list represents
        a row of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # The first row of Pascal's triangle

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Sum 2 el frm prev row
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
