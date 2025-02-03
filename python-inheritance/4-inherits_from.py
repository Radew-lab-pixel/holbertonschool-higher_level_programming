#!/usr/bin/python3
"""inherits_from class"""


def inherits_from(obj, a_class):
    """
    inherits_from - check if obj is a child of a_class
    Args:
        obj : input
        a_class : class reference
    Returns:
        return true of obj is inherited from a_class
    """
    return isinstance(obj, a_class)