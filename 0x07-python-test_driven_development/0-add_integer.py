#!/usr/bin/python3
"""function that adds two ints"""


def add_integer(a, b=98):

    """function that adds two ints"""

    if isinstance(a, float):
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if isinstance(b, float):
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
