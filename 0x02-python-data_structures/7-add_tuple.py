#!/usr/bin/python3
"""adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        new_tup_a = (0, 0)
    if len(tuple_a) == 1:
        new_tup_a = (tuple_a[0], 0)
    if len(tuple_a) >= 2:
        new_tup_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) == 0:
        new_tup_b = (0, 0)
    if len(tuple_b) == 1:
        new_tup_b = (tuple_b[0], 0)
    if len(tuple_b) >= 2:
        new_tup_b = (tuple_b[0], tuple_b[1])
    return tuple(map(lambda x, y: x + y, new_tup_a, new_tup_b))
