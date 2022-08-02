#!/usr/bin/python3
"""returns True if object is an instance of class otherwise False"""


def is_same_class(obj, a_class):
    """function that returns True if object is an instance of class otherwise False"""
    if type(obj) == a_class:
        return True
    else:
        return False
