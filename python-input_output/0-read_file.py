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