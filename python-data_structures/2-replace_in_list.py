#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """replace_in_list function
    replace a element of the list
    Args:
        my_list: list of integer
        idx: location of the element to be replaced
        element: new value of the element

    Returns:
        The return updated my_list
    """
    length = len(my_list)
    if (idx < 0) or (idx >= length):
        return (my_list)
    else:
        temp = my_list
        temp[idx] = element
        return (temp)
