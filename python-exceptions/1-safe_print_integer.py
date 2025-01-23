#!/usr/bin/python3


def safe_print_integer(value):

    try:
        # result = isinstance(value, int)
        # print ("{.d}".format(result))
        print("{.d}".format(value))
        # return (True)
    except Exception as e:
        # except:
        return (False)
    else:
        return (True)
