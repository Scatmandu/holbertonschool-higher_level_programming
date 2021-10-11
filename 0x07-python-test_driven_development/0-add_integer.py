#!/usr/bin/python3
"""function that adds two integers or floats"""


def add_integer(a, b=98):
    """adds two integers or floats"""
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return a + b
