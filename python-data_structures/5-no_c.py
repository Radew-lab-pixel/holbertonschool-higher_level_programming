#!/usr/bin/python3


"""" no_c function

        Args:
        my_string = string input

        Return:
        updated string
    """


def no_c(my_string):

    # copied_string = my_string
    # copied_string = my_string.translate({ord('c'): None})
    # no working on checker
    # copied_string = my_string.translate({ord('C'): None})

    # print(copied_string)
    copied_string = my_string.translate({ord(i): None for i in 'cC'})

    return (copied_string)
