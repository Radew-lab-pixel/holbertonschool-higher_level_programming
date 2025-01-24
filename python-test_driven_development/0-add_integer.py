#!/usr/bin/python3
"""adds integer
"""


def add_integer(a, b=98):
    """
    add_integer - module to add two arguments

    Args:
        a : integer
        b : integer
    Returns:
        sum : integer of a + b
    """
    if not isinstance(a, (int, float)):
        # raise Exception("a must be an integer")
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) == 0):
        raise Exception("b must be an integer")
        # raise TypeError("b must be an integer")
    # else:
    sum = int(a) + int(b)
    return(sum)
