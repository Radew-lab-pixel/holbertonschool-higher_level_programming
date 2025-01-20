#!/usr/bin/python3

""" print_reverse_list function

        Args:
        my_list = list argument

        Returns:
        None
    """


def print_reversed_list_integer(my_list=[]):

    length = len(my_list)
    for i in range(length - 1, -1, -1):
        print("{}".format(my_list[i]))
