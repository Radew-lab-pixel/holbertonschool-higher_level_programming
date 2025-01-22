#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    if (my_list != []):
        try:
            new_list = []
            # lambda (x : length if x > length)
            # limit = lambda x, length: x if x < length else length
            for i in range(0, x, 1):
                new_list.append(my_list[i])
            # new_string = ''.join(new_list)
            new_string = ''.join([str(s) for s in new_list])
            print(int(new_string))
            return (int(i + 1))
        except IndexError:
            # new_string = ''.join(my_list)
            new_string = ''.join([str(s) for s in my_list])
            print(int(new_string))
            length = 0
            for i in new_string:
                length += 1
            return (int(length))
            # print("Index Error")
        # except (ValueError, TypeError) as err:
        except Exception as e:
            print("")
            return (0)
