### Week 16 : Python : Inheritance

### Task 0 : Write a function that returns the list of available attributes and methods of an object:

0-lookup.py
#!/bin/usr/python3

def lookup(obj):
    return dir(obj)

0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass


class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass
print(lookup(MyClass1))
print(lookup(MyClass2))

### Task 1 : Write a class MyList that inherits from list:

1-my_list.py
#!/usr/bin/python3
"""class inheritance from list"""

class MyList(list):   # inherited from list
    """class inheritance from list"""
    def print_sorted(self):
        """public instant method"""
        # print(print_sorted(self))
        # print(sort(self))   # name 'sort' is not defined
        print(sorted(self))
1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

1-my_list.txt

>>> MyList = __import__("1-my_list").MyList
>>> my_list = MyList()
>>> print(my_list)
[]
>>> my_list.print_sorted()
[]
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)
>>> print(my_list)
[1, 4, 2, 3, 5]
>>> my_list.print_sorted()
[1, 2, 3, 4, 5]
>>> print(my_list)
[1, 4, 2, 3, 5]
>>> my_list.append(-7)
>>> print(my_list)
[1, 4, 2, 3, 5, -7]
>>> my_list.print_sorted()
[-7, 1, 2, 3, 4, 5]

### Task 2 : Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False
2-is_same_class.py
#!/usr/bin/python3
"""is_same_class function """

def is_same_class(obj, a_class):
    """is_name_class - check data type of object
    Args:
        obj - input
        a_class - reference datatype
    Returns:
        True if obj match a_class datatype
    """
    # if isinstance(obj, a_class):
    #    return (True)
    # else:
    #    return (False)
    # return isinstance(obj, a_class)
    # print(type(obj) is a_class)
    result = type(obj) is a_class
    return result
2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

### Task 3 : Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
3-is_kind_of_class.py
#!/usr/bin/python3
"""is_kind_of_class"""

 is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - check if obj is class of a_class
    Args:
        obj : input
        a_class : reference class
    """
    return isinstance(obj, a_class)
 
3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

### Task 4 : Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
4-inherits_from.py
#!/usr/bin/python3
"""inherits_from class"""

def inherits_from(obj, a_class):
    """
    inherits_from - check if obj is a child of a_class
    Args:
        obj : input
        a_class : class reference
    Returns:
        return true of obj is inherited from a_class
    """
    # if not (type(obj) == a_class):
    if not (type(obj) is a_class):
        # print(type(obj) == a_class )  # for debugging
        return isinstance(obj, a_class)
    else:
        return False
    # return (issubclass(obj, a_class))

4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

### Task 5 : Write an empty class BaseGeometry.

5-base_geometry.py
#!/usr/bin/python3
""" BaseGeometry class"""

class BaseGeometry:
    """BaseGeometry empty"""
    pass

5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

### Task 6 : Write a class BaseGeometry (based on 5-base_geometry.py).
6-base_geometry.py
#!/usr/bin/python3
""" BaseGeometry class"""
class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """
        area - method
        Args:
            self - instance of area method
        Returns:
            Raise Exception("area() is not implemented")
        """
        return ("[Exception] area() is not implemented")
6-main.py
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

### Task 7 : Write a class BaseGeometry (based on 6-base_geometry.py).
Public instance method: def integer_validator(self, name, value): that validates value:

    you can assume name is always a string
    if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
    if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0

7-base_geometry.py
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
        # if not isinstance(value, int):  # not working in Task 8
        # if (type(value) != int):  # work in Task 8
        if type(value) is not int:  # for task 10
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return True

7-main.py
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

7-base_geometry.txt
>>> bg.integer_validator("width", 89)
True

>>> bg.integer_validator("name", "John")
Traceback (most recent call last):
TypeError: name must be an integer

>>> bg.integer_validator("age", 0)
Traceback (most recent call last):
ValueError: age must be greater than 0

>>> bg.integer_validator("distance", -4)
Traceback (most recent call last):
ValueError: distance must be greater than 0

### Task 8 : Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
    Instantiation with width and height: def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers, validated by integer_validator

8-rectangle.py
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

8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
    # print(issubclass(Rectangle, BaseGeometry))

### Task 9 : Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

9-rectangle.py
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
        return (self.__width * self.__height)

    def __str__(self):
        """return human-readable string representation of an object"""
        # result = []
        result = f"[Rectangle] {self.__width}/{self.__height}"
        return (result)

9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

### Task 10 : Write a class Square that inherits from Rectangle (9-rectangle.py):

10-square.py
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
        # super().__init__(size, size)
        self.integer_validator("size", size)
        # super().integer_validator("size", size)  # for task 10 and 11
        # self.__width = size
        # self.__height = size
        # self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"public method for calculating area"""
        return self.__size * self.__size
        # return self.__width * self.__height

10-main.py
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

### Task 11 - Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
print() should print, and str() should return, the square description: [Square] <width>/<height>

11-square.py
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

        self.integer_validator("size", size)
        # self.__width = size
        # self.__height = size
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"public method for calculating area"""
        return self.__size * self.__size
        # return self.__width * self.__height

    def __str__(self):
        """return human-readable string representation of an object"""
        result = f"[Square] {self.__size}/{self.__size}"
        return result

11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
