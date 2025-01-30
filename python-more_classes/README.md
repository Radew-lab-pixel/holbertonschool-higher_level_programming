### Week 15 : Python - More data structures

## Task 0 - Write an empty class Rectangle that defines a rectangle:

#!/usr/bin/python3
"""0-rectangle.py"""

class Rectangle:
    """ Class of Rectangle object """
    def __init__(self):
        pass

0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

### Task 1 : Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

#!/usr/bin/python3
"""1-rectangle.py"""

class Rectangle:
    """ Class of Rectangle object """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # pass

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

1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

### Task 2 : Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

#!/usr/bin/python3
"""2-rectangle.py"""

class Rectangle:
    """ Class of Rectangle object """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # pass

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

2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

### Task 3 : Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

#!/usr/bin/python3
"""3-rectangle.py"""

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

    def __str__(self):
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

    # def __repr__(self):
        # return repr(self)
    #    result = self.__width + self.__height
    #    return result
        # pass

3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

my_rectangle.width = 0
my_rectangle.height = 4
print(my_rectangle)
print(repr(my_rectangle))

### Task 4 : Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)

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

4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

### Task 5 : Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)

#!/usr/bin/python3
"""5-rectangle.py"""


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
        # Instead of manually converting self.__width and self.__height
        # to strings and concatenating them, the f-string handles this
        # for you, making the code much simpler and easier to read.
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):  # del / destroy
        print(f"Bye rectangle...")

5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:

### Task 6 : How many instances 

#!/usr/bin/python3
"""6-rectangle.py"""

class Rectangle:
    """ Class of Rectangle object """
    # print_area(self)
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        # number_of_instances += 1
        Rectangle.number_of_instances += 1
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
        # Instead of manually converting self.__width and self.__height
        # to strings and concatenating them, the f-string handles this
        # for you, making the code much simpler and easier to read.
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):  # built in del / destroy
        print(f"Bye rectangle...")
        Rectangle.number_of_instances -= 1
        # self.number_of_instances -= 1

        6-main.py

#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

### Task 7 : Public class attribute print_symbol:

    Initialized to #
    Used as symbol for string representation
    Can be any type

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

7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

### Task 8 : Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area

    rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
    rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
    Returns rect_1 if both have the same area value

#!/usr/bin/python3
"""8-rectangle.py"""

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

8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

### Taask 9 : Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size

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

    @classmethod
    def square(cls, size=0):
        # local_size = size
        # cls.width = size  # redudant
        # cls.height = size  # redudant
        # Rectangle(cls.width, cls.height)
        # return Rectangle.
        return cls(size, size)  # cls is the name the class used to call itself
        # instead of return Rectangle (size, size)
        # bob = Rectangle(size, size)

    9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

