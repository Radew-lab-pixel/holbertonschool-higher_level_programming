#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
and then append them to a file:"""
import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """main method that adds all argvs to a python list """
    filename = "add_item.json"

    try:
        # Attempt to load existing data from the file
        text_json = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty list
        text_json = []

    # Append command-line arguments to the list
    # (skip argv[0], which is the script name)
    for i in range(1, len(argv)):
        text_json.append(argv[i])

    # Save the updated list back to the file
    save_to_json_file(text_json, filename)


if __name__ == "__main__":
    main()
