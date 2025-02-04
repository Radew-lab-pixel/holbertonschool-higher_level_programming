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
        super().__init__()  # Call the superclass __init__ method  # remove for task 8
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
