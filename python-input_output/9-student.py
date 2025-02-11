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
