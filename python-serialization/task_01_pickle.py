#!/usr/bin/python3
"""Serialize and deserialize custom Python
objects using the pickle module.
"""
import pickle


class CustomObject:
    """global variable"""
    # name = str
    # age = int
    # is_student = bool

    def __init__(self, name=str, age=int, is_student=bool):
        """constructir"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method to display the object attributes"""
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Is Student : {self.is_student}")

    def serialize(self, filename):
        """method  Using the pickle module, it will
          serialize the current instance of the object a
          nd save it to the provided filename."""
        # text = f"{self.name} {self.age} {self.is_student}"
        # print(text)
        try:
            with open(filename, 'wb') as file:
                # pickle.dump(text, file)
                pickle.dump(self, file)
        except Exception as err:
            print("")

    @classmethod
    def deserialize(cls, filename):
        """class method pickle module, it will load and
        return an instance of the CustomObject from the
        provided filename.
        """
        try:
            with open(filename, 'rb') as file:
                data_loaded = pickle.load(file)
            return data_loaded
        except Exception as err:
            return None
