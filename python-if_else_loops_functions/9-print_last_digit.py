#!/usr/bin/python3


def print_last_digit(number):
    if (number < 0):
        modolus = -1 * number % 10
    else:
        modolus = number % 10
    # return modolus
    print("{0}".format(modolus), end="")
    return modolus
