#!/usr/bin/python3
"""removes all characters c and C from a string"""


def no_c(my_string):
    new_string = ''
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        new_string += x
    return new_string
