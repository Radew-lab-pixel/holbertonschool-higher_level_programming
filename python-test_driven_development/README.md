### Week 14 : Python - Test-driven development

### Task 0 - Write a function that add 2 integers

    0-add_integer.py
#!/usr/bin/python3
"""adds integer
"""


def add_integer(a, b=98):
    """
    add_integer - module to add two arguments

    Args:
        a : integer
        b : integer

    Returns:
        sum : integer of a + b
    """
    if not isinstance(a, (int, float)):
        # raise Exception("a must be an integer")
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) == 0):
        # raise Exception("b must be an integer")
        raise TypeError("b must be an integer")
    # if (isinstance(a, str)):
    #    raise NameError("a must be an integer")
    # if (isinstance(b, str, list, dict)):
    #    raise NameError("b must be an integer")
    # else:
    sum = int(a) + int(b)
    return (sum)
    # return (int(a) + int(b))

    0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print(add_integer(100, "A"))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

    0-add_integer.txt
>>> add_integer = __import__("0-add_integer").add_integer
 >>> add_integer(1, 2)
 3
 >>> add_integer(100, -2)
 98
 >>> add_integer(2)
 100
 >>> add_integer(100.3, -2)
 98
 >>> add_integer(a, 2)
 Traceback (most recent call last):
 NameError: name 'a' is not defined
 >>> add_integer("A", 2)
 Traceback (most recent call last):
 TypeError: a must be an integer
 >>> add_integer(0.0000000000000000007, 2)
 2
 >>> add_integer(float(10**1000), 2)
 Traceback (most recent call last):
 OverflowError: int too large to convert to float

 >>> add_integer(float('inf'))
 Traceback (most recent call last):
 OverflowError: cannot convert float infinity to integer

 >>> add_integer(float('NaN'))
 Traceback (most recent call last):
 ValueError: cannot convert float NaN to integer
 
 ### Task 1 : Write a function that divides all elements of a matrix.

    2-matrix_divided.py
#!/usr/bin/python3
""" matrix_divided """

def matrix_divided(matrix, div):
    """
    function to divide the matrix

    Args:
        matrix : list of integers or float
        div : integer or float

    Returns:
        matrix
    """

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    notNumError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):  # first check if matrix is list
        raise TypeError(notNumError)  # shorten due to pycode said too long
        # res = all(isinstance(ele, list) for ele in matrix)
# if not map(isinstance(lambda i:matrix[i],(float, int)),range(0,num_rows,1)):

    # process matrix
    prev_num_cols = num_cols  # why duplicate as prev code working
    for i in range(0, num_rows, 1):  # go through each row
        if (len(matrix[i]) != prev_num_cols):  # column difference than prev
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(0, len(matrix[i]), 1):   # go through each column
            if not isinstance(matrix[i][j], (float, int)):
                raise TypeError(notNumError)

    # process div
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in lists] for lists in matrix]

    2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

matrix = [
    [1, 2, 'a'],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

    2-matrix_divided.txt

>>> matrix_divided = __import__("2-matrix_divided").matrix_divided
>>> matrix = [[1, 2, 3],[4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

>>> matrix = [[1, 2, 'A'],[4, 5, 6]]

>>> matrix_divided(matrix, 3)
Traceback (most recent call last):
TypeError: matrix must be a matrix (list of lists) of integers/floats

>>> matrix = [[1, 2],[4, 5, 6]]
>>> matrix_divided(matrix, 3)
Traceback (most recent call last):
TypeError: Each row of the matrix must have the same size

>>> matrix = [[1, 2, 3],[4, 5, 6]]
>>> matrix_divided(matrix, 'abc')
Traceback (most recent call last): 
TypeError: div must be a number

>>> matrix_divided(matrix, 0)
Traceback (most recent call last):
ZeroDivisionError: division by zero

>>> matrix_divided(matrix, float('inf'))
[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

>>> matrix_divided(matrix)
Traceback (most recent call last):
TypeError: matrix_divided() missing 1 required positional argument: 'div'


### Task 2 : Write a function that prints My name is <first name> <last name>

    3-say_my_name.py

#!/usr/bin/python3
""" 3-say_my_name """

def say_my_name(first_name, last_name=""):
    """
    function to print the first name and last name

    Args:
        first_name : input of string
        last_name : input of string

    Returns:
        None
    """

    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

    3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

    3-say_my_name.txt
>>> say_my_name = __import__("3-say_my_name").say_my_name
>>> say_my_name("John", "Smith")
My name is John Smith

>>> say_my_name("Walter", "White")
My name is Walter White

>>> say_my_name("Bob")
My name is Bob 

>>> say_my_name("Don", 123)
Traceback (most recent call last):
TypeError: last_name must be a string

>>> say_my_name(123, "Don")
Traceback (most recent call last):
TypeError: first_name must be a string

>>> say_my_name()
Traceback (most recent call last):
TypeError: say_my_name() missing 1 required positional argument: 'first_name'

### Task 3 : Write a function that prints a square with the character #

    4-print_square.py
#!/usr/bin/python3
""" 4-print_square """

def print_square(size):
    """
    function to  print a square with the character #

    Args:
        size : size of length of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer")

    for i in range(0, size, 1):
        for j in range(0, size, 1):
            print("#", end="")
        print()

    4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

    4-print_square.txt
>>> print_square = __import__("4-print_square").print_square
>>> print_square(4)
####
####
####
####

>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

>>> print_square(0)

>>> print_square(-2)
Traceback (most recent call last):
TypeError: size must be >= 0

>>> print_square(0.02)
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square(-0.2)
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square("A")
Traceback (most recent call last):
TypeError: size must be an integer

### Task 4 : Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

    5-text_indentation.py
#!/usr/bin/python3
""" 5-text_indentation.py """


def text_indentation(text):
    """
    function prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
    text : string input

    None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # text_list = list(text.stript())
    text_list = list(text)
    length = len(text_list)

    ref_char = [".", "?", ":"]

    for i in range(0, length, 1):
        print("{}".format(text_list[i]), end="")
        if text_list[i] in ref_char:
            print()  # print two newline
            print()
            # print("\n\n")
            # if (text_list[i + 1]) and (text_list[i + 1] == " "):
            #    text_list[i + 1] = ""  # remove space
            # i += 2
            while (i + 1) < length and text[i + 1] == " ":
                text_list[i + 1] = ""
                i += 1
    # print()

5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

text_indentation("Holberton.School")

text_indentation(12)

    5-text_indentation.txt
>>> text_indentation = __import__("5-text_indentation").text_indentation
>>> text_indentation("Hello World")
Hello World

>>> text_indentation("Hello!, World. How? everyone: today")
Hello!, World.
<BLANKLINE>
How?
<BLANKLINE>
everyone:
<BLANKLINE>
today

>>> text_indentation(12345)
Traceback (most recent call last):
TypeError: text must be a string

>>> text_indentation()
Traceback (most recent call last):
TypeError: text_indentation() missing 1 required positional argument: 'text'

### Task 5: Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.

    6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

    6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))

    6-max_integer_test.py
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def setUp(self):
        self.testListNone = None


    # def test_type(self):

    #    with self.assertRaises(AssertionError):
    #        max_integer([])
    
    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_begin(self):
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_one_neg(self):
        self.assertEqual(max_integer([1, 2, 3, -4, 5]), 5)
    
    def test_max_all_neg(self):
        self.assertEqual(max_integer([-2, -6, -1, -3, -5]), -1)

    def test_max_only_one(self):
        self.assertEqual(max_integer([3]), 3)

    def test_max_none(self):
        # self.assertEqual(max_integer(), 0)
        # with self.assertRaises(AssertionError):
            # max_integer()
            # self.testListNone[:1]
            # self.assertEqual("'NoneType' object is not subscriptable", str(err.exception))
        self.assertEqual(max_integer(), None)