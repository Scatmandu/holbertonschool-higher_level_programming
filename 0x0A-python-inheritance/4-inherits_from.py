#!/usr/bin/python3
"""checks if an object is a subclass"""


def inherits_from(obj, a_class):
    """function that checks if an object is a subclass"""
    if issubclass(type(obj), a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
