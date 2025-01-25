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



