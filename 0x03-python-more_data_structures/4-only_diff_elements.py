#!/usr/bin/python3
"""returns a set of all elements present in only one set"""


def only_diff_elements(set_1, set_2):
    return list(set(set_1) ^ set(set_2))
