#!/usr/bin/python3
import json
"""function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """method to return JSON of object (string)"""
    my_obj_json = json.dumps(my_obj)
    return my_obj_json
