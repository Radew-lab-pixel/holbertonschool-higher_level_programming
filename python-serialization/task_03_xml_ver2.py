#!/usr/bin/python3
"""Module for XML serialization/deserialization"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to an XML file"""
    root_tag = "data"
    root_element = ET.Element(root_tag)
    
    for key, value in dictionary.items():
        child = ET.SubElement(root_element, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root_element)
    tree.write(filename)

def deserialize_from_xml(filename):
    """Deserialize an XML file to a Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    
    result = {}
    for child in root:
        result[child.tag] = child.text
    
    return result