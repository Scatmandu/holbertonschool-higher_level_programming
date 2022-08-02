#!/usr/bin/python3
"""replaces an element in a list at a specific
position without modifying the original list"""


def new_in_list(my_list, idx, element):
    length = len(my_list)
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    elif idx > length:
        return my_list
    else:
        for x in range(length):
            if x == idx:
                new_list[x] = element
                break
        return new_list
