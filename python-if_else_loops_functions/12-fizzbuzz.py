#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 100 + 1, 1):
        modulous_3 = i % 3
        modulous_5 = i % 5
        # if (i != 3) and (i != 5):
        if (modulous_3 == 0 and modulous_5 == 0):
            print("FizzBuzz", end=" ")
            # print("{0}".format(i), end =" ")
        elif modulous_3 == 0 and modulous_5 != 0:
            print("Fizz", end=" ")
        elif modulous_3 != 0 and modulous_5 == 0:
            print("Buxx", end=" ")
        else:
            print("{0}".format(i), end=" ")
