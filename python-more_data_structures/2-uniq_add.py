#!/usr/bin/python3


def uniq_add(my_list=[]):
    # result = functools.reduce()
    # result = map(lambda x : x + y for y in , my_list)
    # return (list(result))
    # result = map(lambda x: x, my_list) # or just sum(my_list)
    # print(list(result))
    # arrange_list = my_list.sort()
    set_list = set(my_list)
    result = sum(set_list)
    # result = sum(my_list)

    return (result)
