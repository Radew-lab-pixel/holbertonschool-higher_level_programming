#!/usr/bin/python3
"""5-square.py"""


class Square:
    """
    Square class

    Attibutes :
    self : an object to refer to itself in Python.
    size : attribute that determine the size

    """
    def __init__(self, size=0, position=(0, 0)):
        # initilization
        self.size = size
        self.position = position

    @property
    def size(self):  # getter method
        return self.__size

    @size.setter
    # def size(self, size):  # setter method
    def size(self, value):
        # if not isinstance(size, int):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        # if size < 0:
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            # self.__size = size
            self.__size = value

    @property       # getting method
    # def position(self, position):
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):   # setter method
        if not isinstance(value[0], int) and not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple) and map(lambda x: x < 0, value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__size, 1):
            for n in range(self.__position[0]):  # add space position
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            # print()
            print("\n", end="")
        # list(map(lambda i: print("#" * self.__size), range(self.__size)))
