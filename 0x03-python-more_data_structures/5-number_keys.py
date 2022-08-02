#!/usr/bin/python3
"""returns the number of keys in a dictionary"""


def number_keys(a_dictionary):
    counter = 0
    for x in a_dictionary:
        counter += 1
    return counter
