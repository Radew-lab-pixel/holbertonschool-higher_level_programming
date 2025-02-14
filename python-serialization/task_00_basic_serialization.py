#!/usr/bin/python3
"""a basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file and deserialize
the JSON file to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    text_json = json.dumps(data, indent=4)
    with open(filename, 'w') as file:
        file.write(text_json)
    # pass


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    with open(filename, 'r') as file:
        result_json = file.read()
    result_str = json.loads(result_json)
    return (result_str)
    # pass
