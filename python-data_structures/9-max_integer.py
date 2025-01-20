#!/usr/bin/python3


def max_integer(my_list=[]):

    if (my_list == "") or (my_list == []):
        return (None)
    else:
        length = len(my_list)
        max = my_list[0]
        for i in range(1, length, 1):
            if (max < my_list[i]):
                max = my_list[i]
        return (max)
