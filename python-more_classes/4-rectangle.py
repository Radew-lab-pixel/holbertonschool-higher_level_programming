#!/usr/bin/python3
"""4-rectangle.py"""


class Rectangle:
    """ Class of Rectangle object """
    # print_area(self)

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # pass
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
                result.append("#")
            # print()
            if i != (self.__height - 1):
                result.append("\n")
        # return ''.join(result)  # convert to string
        return ''.join(map(str, result))  # still worl
        # return str(result)  # won't include \n

    def __repr__(self):  # return raw string
        # WTH WHAT ARE LOOKING FOR ??
        # return repr(self)
        # result = self.__width + self.__height
        # return result
        # pass
        # return str(self.__width + self.__height)
        # return (f"{self.__width}", "{self.__height}")
        # return f"{self.__width}, {self.__height}"
        # -- simplify below
        # rect = "Rectangle(" + str(self.__width)
        # rect += ", " + str(self.__height) + ")"

        # Instead of manually converting self.__width and self.__height
        # to strings and concatenating them, the f-string handles this
        # for you, making the code much simpler and easier to read.
        return f"Rectangle({self.__width}, {self.__height})"
