### Week 17 : Python - Input/Output

## Task 0 : Write a function that reads a text file (UTF8) and prints it to stdout:

0-read_file.py
#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout:"""

def read_file(filename=""):
    """method to read a text file and print it"""
    # file = open(filename, encoding='utf-8')
    # a_string = file.read()
    # print(a_string)
    # file.close()

    with open(filename, 'r') as file:
        a_string = file.read()
        print(a_string, end="")
        # file.close() is not required if using with

0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

## Task 1 : function that writes a string to a text file (UTF8) and returns the number of characters written:

1-write_file.py
#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written"""

def write_file(filename="", text=""):
    """method to write a string to file"""
    with open(filename, 'w') as file:
        file.write(text)
    with open(filename, 'r', encoding='utf-8') as file:
        a_string = file.read()
        return len(a_string)

1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

### Task 2 : Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

2-append_write.py

#!/usr/bin/python3
"""function that appends a string at the end of a
text file (UTF8) and returns the number of characters added:"""

def append_write(filename="", text=""):
    """method that append a string to file"""
    with open(filename, 'a', encoding='utf-8') as file:
        length = len(text)
        # print(text)
        file.write(text)
    return length

2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

###Task 3 : Write a function that returns the JSON representation of an object (string):

3-to_json_string.py
#!/usr/bin/python3
"""function that returns the JSON representation of an object (string):"""
import json


def to_json_string(my_obj):
    """method to return JSON of object (string)"""
    my_obj_json = json.dumps(my_obj)
    return my_obj_json

3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = {
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

## Task 4 : Write a function that returns an object (Python data structure) represented by a JSON string:

4-from_json_string.py
#!/usr/bin/python3
"""function to convert string to JSON format"""
import json

def from_json_string(my_str):
    """method to convert string to JSON format"""
    result = json.loads(my_str)

    return result

4-main.py
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

## Task 5 : Prototype: def save_to_json_file(my_obj, filename):

5-save_to_json.file.py

#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation:"""
import json

def save_to_json_file(my_obj, filename):
    """method to write json file"""
    # serializing my_obj

    # text_json = json.dumps(my_obj, indent=4)
    # with open(filename, 'w') as file:
    #    file.write(text_json)
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
        # json.dump(dictionary, outfile)

5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

## Task 6 : Write a function that creates an Object from a “JSON file”:

6-load_from_json.file.py

#!/usr/bin/python3
"""function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """method that creates an object from JSON file"""
    with open(filename, 'r') as file:
        text_json = file.read()
        # x = json.loads(text_json, object_hook=load_from_json_file)
        x = json.loads(text_json)
        return x
        # print(a_string, end="")

6- main.py

#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

## Task 7 : Write a script that adds all arguments to a Python list, and then save them to a file:

7-add_item.py

#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then append them to a file:"""
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    """main method that adds all argvs to a python list """
    filename = "add_item.json"

    try:
        # Attempt to load existing data from the file
        text_json = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        text_json = []

    # Append command-line arguments to the list
    # (skip argv[0], which is the script name)
    for i in range(1, len(argv)):
        text_json.append(argv[i])

    # Save the updated list back to the file
    save_to_json_file(text_json, filename)

if __name__ == "__main__":
    main()

## Task 8 : Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

8-my_class.py

#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

8-main.py

#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

## Task 9 : Write a class Student that defines a student by:
# Public instance attributes:
#    first_name
#    last_name
#    age

9-student.py

#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """constructor method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """method that return dictionary representation of a Student instance
        to_json - method
        argv :
            self - object passed in
        Return :
            self.__dict__ - dictionary representation of student instances
    """
    def to_json(self):
        return self.__dict__

9-main.py

#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))

## Task 10 : Write a class Student that defines a student by: (based on 9-student.py)
# If attrs is a list of strings, only attribute names contained in this list must be retrieved.
#    Otherwise, all attributes must be retrieved

10-student.py

#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """constructor method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """method that return dictionary representation of a Student instance
        to_json - method
        argv :
            self - object passed in
            attrs - list of strings,
        Return :
            self.__dict__   - if attrs is None, return dict representation
                               of all student instances
                            - else only student instances listed in attrs
    """
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        # if self.__dict__.items()
            # Create an empty dictionary to store the filtered attributes
        filtered_dict = {}  # dict {}

        # Loop through all the attributes of the instance
        for key, value in self.__dict__.items():
            # Check if the current attribute is in the 'attrs' list
            if key in attrs:
                filtered_dict[key] = value
        return filtered_dict

10-main.py
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)

## Task 11 : Write a class Student that defines a student by: (based on 10-student.py)
# Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
#    You can assume json will always be a dictionary
#    A dictionary key will be the public attribute name
#    A dictionary value will be the value of the public attribute

11-student.py
#!/usr/bin/python3
"""class Student that defines a student by"""

class Student:
    """constructor method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """method that return dictionary representation of a Student instance
        to_json - method
        argv :
            self - object passed in
            attrs - list of strings,
        Return :
            self.__dict__   - if attrs is None, return dict representation
                               of all student instances
                            - else only student instances listed in attrs
    """
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        # if self.__dict__.items()
            # Create an empty dictionary to store the filtered attributes
        filtered_dict = {}

        # Loop through all the attributes of the instance
        for key, value in self.__dict__.items():
            # Check if the current attribute is in the 'attrs' list
            if key in attrs:
                filtered_dict[key] = value
        return filtered_dict

    """public method that replaces all attributes of the Student instance"""
    def reload_from_json(self, json):
        for key, value in json.items():
            # self.__dict__.key = value  not working
            setattr(self, key, value)
            # setattr - sets the value of the attribute of an object.

11-main.py
#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

## Task 12 : Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

12-pascal_triangle.py

#!/usr/bin/python3
""" that returns a list of lists of integers representing
the Pascal’s triangle of n:"""

def pascal_triangle(n):
    """
    method for Pascal's Triangle using the nCr (Combination) method.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element is always 1
        for j in range(1, i + 1):
            # Calculate C(i, j) using the previous value in the row
            element = row[j - 1] * (i - j + 1) // j
            row.append(element)
        triangle.append(row)
    return triangle

12-main.py
#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__("12-pascal_triangle").pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

