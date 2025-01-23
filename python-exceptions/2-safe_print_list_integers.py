#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(0, x, 1):
            if (isinstance(my_list[i], int)):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return (count)

    except:
        print()
        return
    # except IndexError:
    #    length = sum(1 for char in my_list)
    #    for i in range(0, length, 1):
    #        if (isinstance(my_list[i], int)):
    #            print("{:d}".format(my_list[i]), end="")
    #            count += 1
    #    print()
    #    return (count)
