#!/usr/bin/python3
def uppercase(str):
    low_to_up = ord('a') - ord('A')
    # str = "Helo World"
    length = len(str)
    
    for i in range (0,length,1):
        str_ord = ord(str[i])
        if (str_ord >= 97 and str_ord <= 122): # lowercase
            str_ord = str_ord - low_to_up
            # str[i] = chr(str_ord) cannot change string variable in Python
        print("{0}".format(chr(str_ord)), end="")

#print("\n")
