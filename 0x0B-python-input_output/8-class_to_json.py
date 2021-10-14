#!/usr/bin/python3
"""returns dictionary description with simple
    data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description"""
    return vars(obj)
