#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) < 123:
        return True
    else:
        return False
    #for i in range(97, 123):
        #ref = chr(i)
    #    ref = i
        # print(f"{ref}", end="")
    #    if chr(ref) == c:
    #        return True
    #return False