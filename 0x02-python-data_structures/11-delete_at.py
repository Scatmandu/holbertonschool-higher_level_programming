#!/usr/bin/python3
"""deletes the item at a specific position in a list"""


def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
