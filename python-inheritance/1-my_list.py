#!/usr/bin/python3
"""class inheritance from list"""


class MyList(list):   # inherited from list
    def print_sorted(self):
        """public instant method"""
        # print(print_sorted(self))
        # print(sort(self))   # name 'sort' is not defined
        print(sorted(self))
