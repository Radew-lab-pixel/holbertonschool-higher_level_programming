#!/usr/bin/python3
"""5-square.py"""


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

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

        # list(map(lambda i: print("#" * self.__size), range(self.__size)))
