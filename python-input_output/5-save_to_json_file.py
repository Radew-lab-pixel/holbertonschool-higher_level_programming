#!/usr/bin/python3
"""function that writes an Object to a text file,
using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """method to write json file"""
    # serializing my_obj

    # text_json = json.dumps(my_obj, indent=4)
    # with open(filename, 'w') as file:
    #    file.write(text_json)
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
        # json.dump(dictionary, outfile)
