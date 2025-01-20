#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    # test_tup1 = (10, 4, 5)
    # test_tup2 = (2, 5, 18)
    # printing original tuples
    # Addition of tuples
    # using map() + zip() + sum()
    # result_a = tuple(map(sum, zip(tuple_a, (0, 0))))
    # result_b = tuple(map(sum, zip(tuple_b, (0, 0))))
    result_a = tuple_a + (0, 0)
    result_b = tuple_b + (0, 0)

    result = tuple(map(sum, zip(result_a, result_b)))
    result_list = list(result)
    result_list = result_list[:2]
    # printing result
    # print("Resultant tuple after addition : " + str(res))
    return(tuple(result_list))
