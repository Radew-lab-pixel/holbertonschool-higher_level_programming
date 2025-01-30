#!/usr/bin/python3
"""7-rectangle.py"""


class Rectangle:
    """ Class of Rectangle object """
    # print_area(self)
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # number_of_instances += 1
        Rectangle.number_of_instances += 1
        # Rectangle.print_symbol = "#"
        # self.print_symbol = "#"
        # self.print_symbol = "#"
    # print_area(self)

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

    def area(self):  # public method to cal area
        return (self.__width * self.__height)

    def perimeter(self):  # public method to cal perimeter
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):   # return readable string
        if self.width == 0:
            return ""
        result = []
        for i in range(0, self.__height, 1):
            for j in range(0, self.__width, 1):
                # print("#", end="")
                # result.append("#")
                # result.append(str(self.__print_symbol))  # default is #
                # result.append(Rectangle.print_symbol)
                result.append(self.print_symbol)
            if i != (self.__height - 1):
                result.append("\n")
        # return ''.join(result)  # convert to string
        return ''.join(map(str, result))  # still worl
        # return str(result)  # won't include \n

    def __repr__(self):  # return raw string
        # Instead of manually converting self.__width and self.__height
        # to strings and concatenating them, the f-string handles this
        # for you, making the code much simpler and easier to read.
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):  # del / destroy
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # def print_symbol(self, value):  # set the symbol
        # self.__print_symbol = value
        # Rectangle.print_symbol = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2
