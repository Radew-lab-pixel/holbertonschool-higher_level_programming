#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    # for value in new_dict.items():
    #    value = value * 2
    new_dict = {key: value * 2 for key, value in new_dict.items()}
    return (new_dict)
