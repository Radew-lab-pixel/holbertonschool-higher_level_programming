#!/usr/bin/python3
"""function that returns the dictionary description with simple data structure"""
import json


def class_to_json(obj):
    """method to turn """
    # text = dict(obj)
    # result = json.loads(obj)
    # return result
    # result = dict(obj)
    # return result
    return obj.__dict__
