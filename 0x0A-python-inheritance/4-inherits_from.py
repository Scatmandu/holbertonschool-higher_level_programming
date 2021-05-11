#!/usr/bin/python3
"""tells if an object's class is inherited"""


def inherits_from(obj, a_class):
    """tells if an object's class is inherited"""

    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class) is True:
        return True
    else:
        return False
