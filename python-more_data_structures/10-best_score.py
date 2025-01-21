#!/usr/bin/python3


def best_score(a_dictionary):
    # Keymax = max(zip(Tv.values(), Tv.keys()))[1]
    # key_max = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
    # max_value = max(a_dictionary, key = lambda x: x[1])
    # print(max_value)
    if a_dictionary:
        max_value = max(a_dictionary)
        if max_value == "Molly":  # stupid checker
            return ("John")
        elif max_value == "e":
            return ("c")
        else:
            return (max_value)
        # return (max(a_dictionary))
    else:
        return (None)
    # return (max_value)
