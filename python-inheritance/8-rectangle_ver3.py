#!/usr/bin/python3
""" BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """
        area - method
        Args:
            self - instance of BaseGeometry
        Returns:
            "[Exception] area() is not implemented"
        """
        raise Exception("area() is not implemented")
        # return ("[Exception] area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - public method that validate value
        Args:
            self - instance of BaseGeometry
            name - input string attribute
            value - input value
        Returns:
            True if value is integer else Raise Exception
        """
        if not isinstance(value, int): # not working in Task 8
        # if not (type(value) == int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return True

# BaseGeometry = BaseGeometry

class Rectangle(BaseGeometry):
    """child class of BaseGeometry"""
    def __init__(self, width, height):
        """Initialize a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            weight (int): The height of the rectangle.
        """
        # Rectangle.integer_validator("width", width)
        # super().__init__()  # Call the superclass __init__ method  # remove for task 8
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
