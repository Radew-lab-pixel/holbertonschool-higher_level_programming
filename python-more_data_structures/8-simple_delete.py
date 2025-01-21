#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    key_check = a_dictionary.get(key)
    # if (key_check != None): # fail pycodestyle but work
    if key_check is not None:
        del a_dictionary[key]
        # a_dictionary.pop(key)
    return (a_dictionary)
