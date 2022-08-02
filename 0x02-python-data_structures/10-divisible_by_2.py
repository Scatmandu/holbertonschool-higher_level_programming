#!/usr/bin/python3
"""finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    new_list = []
    for x in my_list:
        if x % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
