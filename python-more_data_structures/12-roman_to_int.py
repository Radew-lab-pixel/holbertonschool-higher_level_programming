#!/usr/bin/python3


def roman_to_int(roman_string):

    if roman_string:
        roman_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
        roman_list.update({'D': 500, 'M': 1000})  # check say too long

        length = len(roman_string)
        input_list = list(roman_string)

        total_value = 0
        # prev_list_value = roman_list.get(input_list[0])
        # print("Prev_list : {}".format(prev_list_value))
        if (length == 2):  # only two chars
            # [o] < [1] e.g IX
            first_value = (roman_list.get(input_list[0]))  # because tooo long
            second_value = (roman_list.get(input_list[1]))  # because too long
            if first_value < second_value:
                total_value = second_value - first_value
# total_value = roman_list.get(input_list[1]) - roman_list.get(input_list[0])
                return (total_value)
        for i in range(0, length, 1):
            roman_list_value = roman_list.get(input_list[i])
            # if (input_list[i + 1] != None): # in char availabe
            if (i + 1) < length:
                next_list_value = roman_list.get(input_list[i + 1])
                if next_list_value > roman_list_value:  # e.g IX
                    total_value -= roman_list_value  # subtract
                else:
                    total_value += roman_list_value
            else: # last dict key
                total_value = total_value + roman_list_value
            # prev_list_value = roman_list.get(input_list[i])
        return (total_value)
