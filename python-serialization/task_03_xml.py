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