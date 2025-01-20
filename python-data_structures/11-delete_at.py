#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    if (idx < 0) or (my_list == []) or (idx > len(my_list)):
        return (my_list)
    else:
        length = len(my_list)
        result = []
        for i in range(0, length, 1):
            if (i != idx):
                result.append(my_list[i])
        my_list.clear()
        for i in range(0, len(result), 1):
            my_list.append(result[i])
        my_list = result
        return (result)
