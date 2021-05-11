#!/usr/bin/python3
"""find if obj is an instance of/inherited from a_class"""


def is_kind_of_class(obj, a_class):
    """find if obj is an instance of/inherited from a_class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
