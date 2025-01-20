#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if (my_list == []):
        return (None)
    else:
        result = []
        length = len(my_list)
        for i in range (0, length, 1):
            modolus = my_list[i] % 2
            if (modolus == 0):
                result.append(True)
            else:
                result.append(False)
        return (result)
