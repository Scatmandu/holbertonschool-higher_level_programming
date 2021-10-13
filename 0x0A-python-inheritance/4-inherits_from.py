#!/usr/bin/python3
"""checks if an object is a subclass"""


def inherits_from(obj, a_class):
    """it's up there"""
    return issubclass(type(obj), a_class)
