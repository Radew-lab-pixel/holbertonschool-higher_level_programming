#!/usr/bin/python3


# if __name__ == "__main__"
def print_list_integer(my_list=[]):
    """print_list_integer function

    Args:
        my_list = list argument

    Returns:
        None
    """

    # if __name__ == "__main__":
    length = len(my_list)

    for i in range(0, length, 1):
        print("{}".format(my_list[i]))
