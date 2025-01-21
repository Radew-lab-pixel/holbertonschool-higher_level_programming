#!/usr/bin/python3


def common_elements(set_1, set_2):

    # result = list(set(set_1).intersection(set_2)) # working too or
    # print (result)
    result = set(set_1) & set(set_2)
    # print (result)
    return (result)
