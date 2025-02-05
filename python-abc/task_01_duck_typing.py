#!/usr/bin/python3
from abc import ABC, abstractmethod
"""abstract class Shape using ABC package"""


class Shape(ABC):
    """abstract class named Shape"""
    @abstractmethod
    def area(self):
        """abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method perimeter"""
        pass


class Circle(Shape):
    """subclass 1 named Circle of class Shape"""
    # pi = 3.141592653589793
    def __init__(self, radius):
        """constructor of Circle subclass"""
        # self.__radius = radius
        self.pi = 3.141592653589793
        self.radius = radius

    def area(self):
        """method of Circle to cal area"""
        # print(f"Area: {self.radius * self.radius * self.pi}")
        return self.radius * self.radius * self.pi

    def perimeter(self):
        """method of Circle to cal perimeter"""
        # print(f"Perimeter: {2 * self.radius * self.pi}")
        return 2 * self.radius * self.pi


class Rectangle(Shape):
    """subclass 2 named Rectangle of class Shape """
    def __init__(self, width, height):
        """constructor of Rectangle subclass"""
        # self.__width = width
        # self.__height = height
        self.width = width
        self.height = height

    def area(self):
        """method of Rectangle to cal area"""
        # print(f"Area: {self.width * self.height}")
        return self.width * self.height

    def perimeter(self):
        """method of Rectangle to cal perimeter"""
        # print(f"Perimeter: {2 * (self.width + self.height)}")
        return 2 * (self.width + self.height)

# Attributes having same name are
# considered as duck typing
# for obj in Circle(), Rectangle():
#    obj.area()
#    obj.perimeter()


def shape_info(obj):
    """public function shape_info duck typing"""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
