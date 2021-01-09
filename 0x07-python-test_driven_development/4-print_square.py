#!/usr/bin/python3
"""this module prints a square with the method print_square"""


def print_square(size):
    """
    prints a square based on size using #


    Arguments:
        size (int) - how large to print the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print()
    if type(size) is int:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
