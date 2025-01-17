#!/usr/bin/python3

def islower(c):
    for i in range(97, 123):
        #ref = chr(i)
        ref = i
        # print(f"{ref}", end="")
        if chr(ref) == c:
            return True
    return False

