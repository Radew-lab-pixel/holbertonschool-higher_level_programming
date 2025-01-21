Week 14 - More Data Structures : Set and Dictionary
### Task 0

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    new_matrix = [[0 for x in range(num_cols)] for y in range(num_rows)]

    for i in range(0, num_rows, 1):
        for j in range(0, num_cols, 1):
            new_matrix[i][j] = matrix[i][j] ** 2
    return (new_matrix)

0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

### Task 1

#!/usr/bin/python3

def search_replace(my_list, search, replace):

    length = len(my_list)
    # new_list = my_list
    new_list = my_list.copy()

    if (length < search):
        return (new_list)
    else:
        for i in range(0, length, 1):
            if (new_list[i] == search):
                new_list[i] = replace
        return (new_list)

1-main.py

#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

### Task 2

#!/usr/bin/python3

def uniq_add(my_list=[]):
    # result = functools.reduce()
    # result = map(lambda x : x + y for y in , my_list)
    # return (list(result))
    # result = map(lambda x: x, my_list) # or just sum(my_list)
    # print(list(result))
    # arrange_list = my_list.sort()
    set_list = set(my_list)
    result = sum(set_list)
    # result = sum(my_list)

    return (result)

    2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
