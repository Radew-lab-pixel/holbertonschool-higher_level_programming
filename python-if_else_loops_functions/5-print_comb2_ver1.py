#!/usr/bin/python3

for i in range(0, 99):
    if i < 10:
        print("0", end="")
    # pfrint("{0}".format(i), end=", ")
    match i:
        case 99:
            ending = "\n"
        case _: # other
            ending = ", "
    print("{0}".format(i), end=ending)

    