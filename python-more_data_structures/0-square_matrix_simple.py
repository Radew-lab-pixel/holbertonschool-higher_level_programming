#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    new_matrix = [[0 for x in range(num_cols)] for y in range(num_rows)]

    for i in range(0, num_rows, 1):
        for j in range(0, num_cols, 1):
            new_matrix[i][j] = matrix[i][j] ** 2
    return (new_matrix)
