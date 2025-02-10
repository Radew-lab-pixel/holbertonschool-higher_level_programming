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
