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

### Task 2 : Write a class Square that defines a square by: (based on 1-square.py)

2-square.py

#!/usr/bin/python3
"""2-square.py"""

class Square:
    """
    Square class

    Attibutes :
    self : an object to refer to itself in Python.
    size : attribute that determine the size

    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        2-main.py

#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
    
### Task 3 : Write a class Square that defines a square by: (based on 2-square.py)

3-square.py

#!/usr/bin/python3
"""3-square.py"""

class Square:
    """
    Square class

    Attibutes :
    self : an object to refer to itself in Python.
    size : attribute that determine the size

    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

        3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

### Task 4 : Write a class Square that defines a square by: (based on 3-square.py)

4-square.py

#!/usr/bin/python3
"""4-square.py"""

class Square:
    """
    Square class

    Attibutes :
    self : an object to refer to itself in Python.
    size : attribute that determine the size

    """
    def __init__(self, size=0):
        # initilization
        self.size = size

    @property
    def size(self):  # getter method
        return self.__size

    @size.setter
    def size(self, size):  # setter method
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size * self.__size)

        4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

    4-main.py
    
