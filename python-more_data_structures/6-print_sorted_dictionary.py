#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    # reference from :
    # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    sorted_dict = dict(sorted(a_dictionary.items(), reverse=False))
    # length = len(sorted_dict)
    # for i in range(0, length, 1):
    #    print(sorted_dict[i])
    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
    # print(sorted_dict)
    # return (sorted_dict)
