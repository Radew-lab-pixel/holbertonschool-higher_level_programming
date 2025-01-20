#!/usr/bin/python3


def max_integer(my_list=[]):

    if (my_list == ""):
        return (None)
    else:
        length = len(my_list)
        max = 0
        for i in range(0, length, 1):
            if (max < my_list[i]):
                max = my_list[i]
        return (max)
