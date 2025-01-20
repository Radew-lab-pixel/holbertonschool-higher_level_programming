#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    """" print_matrix_integer function
        
        Args:
        matrix = array input

        Return:
        none
    """

    num_rows =  len(matrix)
    num_cols = len(matrix[0])
    # print(num_cols)
    # print(num_rows)

    for i in range(0, num_rows, 1):
        for j in range(0, num_cols, 1):
            if (j < num_cols - 1):
                print("{}".format(matrix[i][j]), end = " ")
            else:
                print("{}".format(matrix[i][j]), end = "")
                print()
