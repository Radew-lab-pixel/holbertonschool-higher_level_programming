#!/usr/bin/python3
"""is_same_class function """


def is_same_class(obj, a_class):
    """is_name_class - check data type of object
    Args:
        obj - input
        a_class - reference datatype
    Returns:
        True if obj match a_class datatype
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)

