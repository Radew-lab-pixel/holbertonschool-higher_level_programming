Week 14 : Python - Exceptions
# Task 0 Write a function that prints x elements of a list.

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
    else:
        print("")
        return (0)


0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
my_list1 = []
nb_print = safe_print_list(my_list1, 0)
print("nb_print: {:d}".format(nb_print))

## Task 1 : Write a function that prints an integer with "{:d}".format().

#!/usr/bin/python3


def safe_print_integer(value):

    try:
        # result = isinstance(value, int)
        # print ("{:d}".format(result))
        print("{:d}".format(value))
        # return (True)
    except Exception as e:
        # except:
        return (False)
    else:
        return (True)

## Task 2 Write a function that prints the first x elements of a list and only integers.

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

    except IndexError:
        # print("")
        return
    # except IndexError:
    #    length = sum(1 for char in my_list)
    #    for i in range(0, length, 1):
    #        if (isinstance(my_list[i], int)):
    #            print("{:d}".format(my_list[i]), end="")
    #            count += 1
    #    print()
    #    return (count)

2-main.py

#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

mylist = [1, 2, 3, 4]
nb_print = safe_print_list_integers(my_list, len(mylist) + 4)
print("nb_print: {:d}".format(nb_print))

### Task 3 : Write a function that divides 2 integers and prints the result.

#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except Exception as e:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)

3-main.py

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

### Task 4 : Write a function that divides element by element 2 lists.

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

4-main.py

#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

### Task 5 : Write a function that raises a type exception.

#!/usr/bin/python3


def raise_exception():
    a = 10
    b = "2"
    result = a / b
    print(result)


5-main.py

#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

### Task 6 : Write a function that raises a name exception with a message.

#!/usr/bin/python3

def raise_exception_msg(message=""):
    raise NameError(message)
    # print(string.ascii_letters)

6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
