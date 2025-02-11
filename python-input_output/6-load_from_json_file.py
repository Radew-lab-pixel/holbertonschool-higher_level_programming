#!/usr/bin/python3
"""function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        text_json = file.read()
        # x = json.loads(text_json, object_hook=load_from_json_file)
        x = json.loads(text_json)
        return x
        # print(a_string, end="")