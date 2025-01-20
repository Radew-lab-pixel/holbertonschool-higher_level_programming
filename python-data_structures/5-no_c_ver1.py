#!/usr/bin/python3


"""" no_c function
        
        Args:
        my_string = string input

        Return:
        updated string
    """

def no_c(my_string):
    
    #temp = my_string
    my_list = list(my_string) # convert string to list
    length = len(my_list)
    if (length > 0):
        #for i in range(0, length - 1, 1):
        i = 0
        while (i < length - 1):
            
            my_list.remove('c')
            # my_list.remove('C')
         
            length = len(my_list)
            i+=1
        #return (my_string)
        updated_string = ''.join(my_list)
    return(updated_string)