#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """method to read a text file and print it"""
    file = open(filename, encoding='utf-8')
    a_string = file.read()
    print(a_string)
