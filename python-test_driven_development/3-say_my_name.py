#!/usr/bin/python3
""" 3-say_my_name """


def say_my_name(first_name, last_name=""):
    """
    function to print the first name and last name

    Args:
        first_name : input of string
        last_name : input of string

    Returns:
        None
    """

    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
