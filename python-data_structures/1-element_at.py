#!/usr/bin/python3


def element_at(my_list, idx):
    """element_at function
        display element
    Args:
        my_list: list of integer
        idx: location of the element

    Returns:
        The return value of my_list[idx]
    """
    # if __name__== "__main__":

    length = len(my_list)

    if (idx < 0 or idx >= length):
        return("None")
    else:
        return(my_list[idx])
