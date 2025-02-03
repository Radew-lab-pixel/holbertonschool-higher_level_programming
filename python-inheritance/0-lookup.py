#!/usr/bin/python3
""" method that return a list of attributes
and methods of an object """


def lookup(obj):
    """ lookup : method that return a list of attributes """
    """
    Args:
        obj : input
    """
    return dir(obj)
