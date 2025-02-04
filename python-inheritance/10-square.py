#!/usr/bin/python3
""" child class of Square inherited from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """child Square inherited from Rectangle"""
    def __init__(self, size):
        """ Initialize a Square instance.
            Args:
                size (int): The width of the Square.
        """
        # super().__init__(size, size)  # initalize the parent instance
        super().__init__(size, size)
        name = "size"
        self.integer_validator(name, size)
        # self.__width = size
        # self.__height = size
        self.__size = size

    def area(self):
        """"public method for calculating area"""
        return self.__size * self.__size
        # return self.__width * self.__height
