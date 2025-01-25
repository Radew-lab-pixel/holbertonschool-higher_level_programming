#!/usr/bin/python3
""" matrix_divided """


def matrix_divided(matrix, div):
    """
    function to divide the matrix

    Args:
        matrix : list of integers or float
        div : integer or float

    Returns:
        matrix
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    notNumError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):  # first check if matrix is list
        raise TypeError(notNumError)  # shorten due to pycode said too long
        # res = all(isinstance(ele, list) for ele in matrix)
# if not map(isinstance(lambda i:matrix[i],(float, int)),range(0,num_rows,1)):

    # process matrix
    prev_num_cols = num_cols  # why duplicate as prev code working
    for i in range(0, num_rows, 1):  # go through each row
        if (len(matrix[i]) != prev_num_cols):  # column difference than prev
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, len(matrix[i]), 1):   # go through each column
            if not isinstance(matrix[i][j], (float, int)):
                raise TypeError(notNumError)

    # process div
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in lists] for lists in matrix]
