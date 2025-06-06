#!/usr/bin/python3
"""reading data from one format (CSV) and 
converting it into another format (JSON) using 
serialization techniques.
"""
import csv
import json


def convert_csv_to_json(filename_csv):
    """method that takes the CSV filename as its parameter 
    and writes the JSON data to data.json."""
    # step 1
    data_dict = {}  # create empty dict attribute

    # step 2 open csv file handler
    with open(filename_csv, 'r', encoding='utf-8') as file_csv:
        # read file_csv to csv_reader pior to convert to dict
        csv_reader = csv.DictReader(file_csv, delimiter=',')
        # convert each row into a dict and add converted data
        # to data variable
        for rows in csv_reader:
            # column named 'name' in data.csv is the primary key
            # 1st row is header
            # key = rows['name']  # 1st row 1st column is 'name'
            # key = rows['name']
            data_dict[key] = rows  # auto assign value to resective key

    # open a json file handler and use json dumps
    # to convert dict to json string
    filename_json = "data.json"
    with open(filename_json, 'w', encoding ='utf-8') as file_json:
        # step 3 : json dumps to convert dict to json string
        file_json.write(json.dumps(data_dict, indent=4))
