#!/usr/bin/python3
""" 4-print_square """


def print_square(size):
    """
    function to  print a square with the character #

    Args:
        size : size of length of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer")

    for i in range(0, size, 1):
        for j in range(0, size, 1):
            print("#", end="")
        print()
