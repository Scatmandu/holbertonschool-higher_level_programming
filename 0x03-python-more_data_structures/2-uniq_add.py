#!/usr/bin/python3
"""adds all unique integers in a list (only once for each integer)"""


def uniq_add(my_list=[]):
    new_list = []
    numby_store = 0
    for x in my_list:
        if x not in new_list:
            new_list.append(x)
    for y in new_list:
        numby_store += y
    return numby_store
