#!/usr/bin/python3
""" that returns a list of lists of integers representing
the Pascal’s triangle of n:"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle using the nCr (Combination) method.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        for j in range(1, i + 1):
            # Calculate C(i, j) using the previous value in the row
            element = row[j - 1] * (i - j + 1) // j
            row.append(element)
        triangle.append(row)
    return triangle
