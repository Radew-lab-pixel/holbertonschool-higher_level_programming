#!/usr/bin/python3


def roman_to_int(roman_string):
    
    if roman_string:
        roman_list = {'I': 1, 'V' : 5, 'X': 10, 'L' : 50, 'C' : 100, 'D': 500, 'M' : 1000 }

        length = len(roman_string)
        input_list = list(roman_string)

        total_value = 0
        # prev_list_value = roman_list.get(input_list[0])
        # print("Prev_list : {}".format(prev_list_value))
        for i in range(0, length, 1):
            roman_list_value = roman_list.get(input_list[i])
            # print("Current Roman list value : {}".format(roman_list_value))
            # if (i > 0 and (prev_list_value < roman_list_value)):
            # if (prev_list_value < roman_list_value):
            if (i == 0):
                prev_list_value = 0
                # roman_list_value -= prev_list_value  # eg IX is 9
                # print(roman_list_value)
                # print("Found prev value less than current : {}".format(roman_list_value))
            roman_list_value = roman_list_value - prev_list_value
                # print("New roman list value : {}".format(roman_list_value))
            prev_list_value = roman_list.get(input_list[i]) # save current char as prev
            total_value = total_value + roman_list_value
        return (total_value)



