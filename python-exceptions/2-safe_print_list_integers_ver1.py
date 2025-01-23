#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try :
        new_list = []        
        for i in range(0, x, 1):
            new_list.append(my_list[i])
        new_string = ''.join([str(s) for s in new_list])
        # print(new_string)
        print("{:d}".format(new_string))
        return(int(i + 1))
    except Exception as e:
        my_list_ok = [ val for val in my_list if isinstance(val, int)]
        new_list = []
        for i in range(0, x, 1):
            new_list.append(my_list_ok[i])
        new_string = ''.join([str(s) for s in new_list])
        print("{:d}".format(int(new_string)))
        return(int(i + 1))    
    
    # else:
        # print(new_string)
        # print("{:d}".format(int(new_string)))
        # return(int(i + 1))
  