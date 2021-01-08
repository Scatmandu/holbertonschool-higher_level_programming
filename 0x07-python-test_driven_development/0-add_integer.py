#!/usr/bin/python3
"""sums two floats or integers"""


def add_integer(a, b=98):
    """
    ``add_integer`` - sums two numbers


    Arguments:
        a - an int or float
        b - an int or float


    Returns:
        the sum of a and b
    """
    if type(a) is float:
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
