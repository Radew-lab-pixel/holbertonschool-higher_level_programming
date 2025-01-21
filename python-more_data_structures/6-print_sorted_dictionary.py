#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    # reference from :
    # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    sorted_dict = dict(sorted(a_dictionary.items(), reverse=False))
    print(sorted_dict)
    # return (sorted_dict)
