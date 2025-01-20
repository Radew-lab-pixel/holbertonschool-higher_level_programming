#!/usr/bin/python3

""" new_in_list function

        Args:
        my_list = list argument
        idx: index of the list
        element: value of the index of the list

        Returns:
        new updated list
"""


def new_in_list(my_list, idx, element):

    temp = my_list
    length = len(temp)

    if (idx < 0 or idx >= length):
        return (temp)
    else:
        copied_list = temp.copy()
        copied_list[idx] = element
        return (copied_list)
