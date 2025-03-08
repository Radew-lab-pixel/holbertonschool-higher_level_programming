###Week 17- Serialization

##Task 0 : Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

## task_00_basic_serialization.py
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

    0-main.py
    #!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)

## Task 1 : Learn how to serialize and deserialize custom Python objects using the pickle module.

task_01_pickle.py
#!/usr/bin/python3
"""Serialize and deserialize custom Python
objects using the pickle module.
"""
import pickle


class CustomObject:
    """global variable"""
    # name = str
    # age = int
    # is_student = bool

    def __init__(self, name=str, age=int, is_student=bool):
        """constructir"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """method to display the object attributes"""
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Is Student : {self.is_student}")

    def serialize(self, filename):
        """method  Using the pickle module, it will
          serialize the current instance of the object a
          nd save it to the provided filename."""
        # text = f"{self.name} {self.age} {self.is_student}"
        # print(text)
        try:
            with open(filename, 'wb') as file:
                # pickle.dump(text, file)
                pickle.dump(self, file)
        except Exception as err:
            print("")

    @classmethod
    def deserialize(cls, filename):
        """class method pickle module, it will load and
        return an instance of the CustomObject from the
        provided filename.
        """
        try:
            with open(filename, 'rb') as file:
                data_loaded = pickle.load(file)
            return data_loaded
        except Exception as err:
            return None

1-main.py
#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()

## Task 2 The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

task_02_csv.py
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
    # data_dict = {}  # create empty dict attribute
    data_list = [] # create a list to avoid the adding 1st key('name') to data_dict

    # step 2 open csv file handler
    try:
        with open(filename_csv, 'r', encoding='utf-8') as file_csv:
            # read file_csv to csv_reader pior to convert to dict
            csv_reader = csv.DictReader(file_csv, delimiter=',')
            # convert each row into a dict and add converted data
            # to data variable
            for rows in csv_reader:
                # column named 'name' in data.csv is the primary key
                # 1st row is header
                # key = rows['name']  # 1st row 1st column is 'name'
                # data_dict[key] = rows  # auto assign value to resective key
                data_list.append(rows)  # Append entire row to the list
    except Exception as err:
        print("")
        return False

    # open a json file handler and use json dumps
    # to convert dict to json string
    filename_json = "data.json"
    try:
        with open(filename_json, 'w', encoding='utf-8') as file_json:
            # step 3 : json dumps to convert dict to json string
            # file_json.write(json.dumps(data_dict, indent=4))
            file_json.write(json.dumps(data_list, indent=4))
            return True
    except Exception as err:
        return False

        2-main.py
     #!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")

data.csv
name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco

data.json
[
    {
        "name": "John",
        "age": "28",
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": "24",
        "city": "Los Angeles"
    },
    {
        "name": "Bob",
        "age": "22",
        "city": "Chicago"
    },
    {
        "name": "Eve",
        "age": "30",
        "city": "San Francisco"
    }
]

## Task 3 : In this exercise we’ll explore serialization and deserialization using XML as an alternative format to JSON.

task_03_xml.py

#!/usr/bin/python3
"""function to serialization and deserialization
using XML as an alternative format to JSON"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """method to Python dictionary and a filename as parameters.
    It should serialize the dictionary into XML and save it
    to the given filename."""
    
    # parse XML to into element tree
    # tree = ET.parse(filename)
    # root = tree.getroot()

    # xml format
    root_tag = "data"  # root name 
    elem = ET.Element(root_tag)

    for key, val in dictionary.items(): #
        # create an element
        # class object
        child = ET.Element(key)
        child.text = str(val)
        elem.append(child)
 
    """ # this function work
        for key, value in dictionary.items():
        child = ET.SubElement(elem, key)
        child.text = str(value)
    """    
    tree = ET.ElementTree(elem)
    tree.write(filename)
   

def deserialize_from_xml(filename):
    """method to take a filename as its parameter,
      read the XML data from that file, and
      return a deserialized Python dictionary."""
    
    # data_xml = ET.fromstring(filename)
    # parse xml to Elemtn Tree
    tree = ET.parse(filename)
    root = tree.getroot()

    result={}
    # loop over children
    for child in root:
        # child_data = child.tag
        result[child.tag] = child.text
    
    return result

    3-main.py
    from task_03_xml_ver1 import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()

    data.xml
<data><name>John</name><age>28</age><city>New York</city></data>