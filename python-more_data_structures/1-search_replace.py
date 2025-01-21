#!/usr/bin/python3


def search_replace(my_list, search, replace):

    length = len(my_list)
    # new_list = my_list
    new_list = my_list.copy()

    if (length < search):
        return (new_list)
    else:
        new_list[search] = replace
        return (new_list)
