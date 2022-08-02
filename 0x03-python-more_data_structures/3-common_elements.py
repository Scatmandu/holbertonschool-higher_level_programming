#!/usr/bin/python3
"""returns a set of common elements in two sets"""


def common_elements(set_1, set_2):
    new_set = set()
    for x in set_1:
        for y in set_2:
            if x == y:
                new_set.add(y)
    return new_set
