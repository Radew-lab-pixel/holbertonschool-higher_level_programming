#!/usr/bin/python3

import sys

n = len(sys.argv)
if (n == 2):
    print("{} argument:".format(n - 1))
elif (n == 1):  # zero arguemnt
    print("{} arguments.".format(n - 1))
else:
    print("{} arguments:".format(n-1))
if n > 1:
    for i in range(1, n, 1):
        print("{}: {}".format(i, sys.argv[i]))
