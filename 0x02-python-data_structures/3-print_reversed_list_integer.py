#!/usr/bin/python3
"""prints all integers of a list in reverse order"""


def print_reversed_list_integer(my_list=[]):
    if my_list:
        for x in my_list[::-1]:
            print("{:d}".format(x))
