#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    # print(dir(hidden_4))
    name = dir(hidden_4)
    # length = len(name)
    # for i in range(0, length, 1):
    for i in name:
        if i[0:2] != "__":
            print("{}".format(i))
