#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    new_matrix=[]

    for i in range(0, num_rows - 1, 1):
        for j in range(0, num_cols, 1):
            new_matrix.append(matrix[i][j] * matrix[i][j])
    return (list(new_matrix))

