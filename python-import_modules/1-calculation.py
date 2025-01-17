#!/usr/bin/python3

if __name__ == "__main__":
"""Print the sum, difference, multiple and quotient of 10 and 5."""

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result_sum = add(10, 5)
    print("{}".format(a), "+ {}".format(b), "= {}".format(result_sum))
    result_sub = sub(10, 5)
    print("{}".format(a), "- {}".format(b), "= {}".format(result_sub))
    result_mul = mul(10, 5)
    print("{}".format(a), "* {}".format(b), "= {}".format(result_mul))
    result_div = div(10, 5)
    print("{}".format(a), "/ {}".format(b), "= {}".format(result_div))

