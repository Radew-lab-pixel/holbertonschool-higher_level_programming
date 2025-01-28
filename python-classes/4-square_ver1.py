#!/usr/bin/python3
"""4-square.py"""


class Square:
    """
    Square class

    Attibutes :
    self : an object to refer to itself in Python.
    size : attribute that determine the size

    """
    def __init__(self, size=0):
        # initilization
        self.size = size

    @property
    def size(self):  # getter method
        return self.__size

    @size.setter
    def size(self, size):  # setter method
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)
