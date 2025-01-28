Week 15 - Python - Classes and Objects

Task 0 : Write an empty class Square that defines a square:

0-square.py 

#!/usr/bin/python3
""" 0-square.py """

class Square:
    """ Square class object

        Attributes:
        self : custom class used to access the class’s members and
        methods, as well as to create new members
    """
    def __init__(self):
        # attributes below like structure in c, dict in python
        # self.size = 0
        # self.width = width
        # self = width
        self = 0

0-main.py

#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

### Task 1 : Square with size 

1-square.py

!/usr/bin/python3
"""1-sqaure.py"""

class Square:
    """ Square class object

        Attributes:
        self : custom class used to access the class’s members and
        methods, as well as to create new members
        size : size of the square
    """
    def __init__(self, size):

        # if __name__ = '__main__':
        self.__size = size

        1-main.py

        !/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
