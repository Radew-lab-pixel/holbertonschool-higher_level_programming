#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    a_copy = tuple_a
    b_copy = tuple_b 
    # b_list = list(tuple_b)

    # a_list = a_list + (0, 0)
    # b_list = b_list + (0, 0)
    
    # a_copy = zip(a_copy, (0, 0))
    # b_copy = zip(a_copy, (0, 0))

    a_copy = a_copy + (0, 0)
    b_copy = b_copy + (0, 0)

    # print(a_copy)
    result = map(lambda x, y: x + y, a_copy, b_copy)
    result = tuple(result)
    return(result)
