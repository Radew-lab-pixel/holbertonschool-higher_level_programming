#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    for i in range(0, list_length, 1):
        try:
            # new_list = []
            # for i in range(0, list_length, 1):
            result = my_list_1[i] / my_list_2[i]
            # new_list.append(result[i])
            # return (new_list)

        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
