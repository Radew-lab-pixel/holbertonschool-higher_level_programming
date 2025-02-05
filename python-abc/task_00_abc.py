#!/usr/bin/python3
from abc import ABC, abstractmethod
"""create an abstract class named Animal"""


class Animal(ABC):
    """Abstract class named Animal"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """subclass named Dog of Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """subclass named Cat of Animal"""
    def sound(self):
        return "Meow"
