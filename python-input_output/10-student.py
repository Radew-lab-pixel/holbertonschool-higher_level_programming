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
