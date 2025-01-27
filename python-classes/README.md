Week 15 - Python - Classes and Objects

Task 0 : Write an empty class Square that defines a square:

0-square.py 

#!/usr/bin/python3
""" 0-square.py """


class Square:
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