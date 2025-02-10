#!/usr/bin/python3
"""function to convert string to JSON format"""
import json


def from_json_string(my_str):
    """method to convert string to JSON format"""
    result = json.loads(my_str)
    return result
