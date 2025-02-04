#!/usr/bin/python3
""" BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class of BaseGeometry"""
    def __init__(self, width, height):
        """Initialize a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            weight (int): The height of the rectangle.
        """
        # Rectangle.integer_validator("width", width)
        super().__init__()  # Call the superclass __init__ method
        self.integer_validator("width", width)
        # self.width = width
        self.__width = width  # private attribute
        self.integer_validator("height", height)
        # self.height = height
        self.__height = height  # private attribute

    def area(self):  # public method
        """public method to cal area"""
        print(self.__width * self.__height)

    def __str__(self):
        """return human-readable string representation of an object"""
        # result = []
        result = f"[Rectangle] {self.__width}/{self.__height}"
        return (result)
