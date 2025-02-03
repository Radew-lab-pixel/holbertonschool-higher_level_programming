#!/usr/bin/python3

class lookup:  # parent class
    def __init__(self, obj):
        self.obj = obj

    @property
    def obj(self):
        return (dir(self.__obj))

    @obj.setter
    def obj(self, value):  # setter method
        self.__obj = value
