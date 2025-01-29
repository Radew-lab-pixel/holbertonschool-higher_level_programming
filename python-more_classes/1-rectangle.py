#!/usr/bin/python3
"""1-rectangle.py"""


class Rectangle:
    """ Class of Rectangle object """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # pass

    @property
    def width(self):  # Getter for width
        return (self.__width)

    @width.setter
    def width(self, value):  # setter method
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):  # Getter for height
        return self.__height

    @height.setter
    def height(self, value):  # setter for height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
