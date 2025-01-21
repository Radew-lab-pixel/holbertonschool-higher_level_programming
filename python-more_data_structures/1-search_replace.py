#!/usr/bin/python3


def search_replace(my_list, search, replace):

    length = len(my_list)
    # new_list = my_list
    new_list = my_list.copy()

    if (length < search):
        return (new_list)
    else:
        for i in range(0, length, 1):
            if (new_list[i] == search):
                new_list[i] = replace
        return (new_list)
# working 
# def search_replace(my_list, search, replace):
#    return [[num, replace][num is search] for num in my_list]