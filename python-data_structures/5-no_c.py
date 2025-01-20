#!/usr/bin/python3


"""" no_c function

        Args:
        my_string = string input

        Return:
        updated string
    """


def no_c(my_string):

    # copied_string = my_string
    copied_string = my_string.translate({ord('c'): None})
    copied_string = my_string.translate({ord('C'): None})
    # print(copied_string)

    return (copied_string)
