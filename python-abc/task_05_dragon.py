#!/usr/bin/python3
"""Mixins class """

class SwimMixin:
    """parent class SiwimMixin """

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """parent class FlyMixin"""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """child class Dragon"""

    def roar(self):
        """child method roar"""
        print("The dragon roars!")
