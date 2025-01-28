#!/usr/bin/python3
"""1-sqaure.py"""


class Square:
    """ Square class object

        Attributes:
        self : custom class used to access the class’s members and
        methods, as well as to create new members
        size : size of the square
    """
    def __init__(self, size):

        # if __name__ = '__main__':
        self.__size = size
