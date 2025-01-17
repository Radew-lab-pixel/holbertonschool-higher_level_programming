#!/usr/bin/python3


def pow(a, b):
    result = a
    b_copy = b
    if b_copy == 0:
        return (1)
    elif b_copy < 0:
        b = b * -1

    for i in range(1, b, 1):
        result = result * a
    if b_copy < 0:
        result = 1 / result
    return (result)
