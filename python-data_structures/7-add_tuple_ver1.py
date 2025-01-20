#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    length_a =  len(tuple_a)
    # length_b = len(tuple_b)

    result = []
    for i in range(0, length_a - 1, 1):
        result.append(tuple_a[i] + tuple_b[i])
    result = tuple(result)

    return(result)
