#!/usr/bin/python3
"""check if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """checks if object is an instance of a class"""

    if type(obj) is a_class:
        return True
    else:
        return False
