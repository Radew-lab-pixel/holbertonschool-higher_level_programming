#!/usr/bin/python3

for i in range(1, 100):
    remain = int(i % 10)
    whole = int(i/10)
    swap_i = (remain * 10) + whole
    # print(f"{swap_i}")
    if i < 10:
        print("0", end="")
        # pfrint("{0}".format(i), end=", ")
    if i == 89:
        ending="\n"
    else:
        ending=", "
    if i < swap_i:
        print("{0}".format(i), end=ending)
