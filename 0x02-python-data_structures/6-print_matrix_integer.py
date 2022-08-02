#!/usr/bin/python3
"""prints a matrix of integers"""


def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for value in row:
            i += 1
            if i == len(row):
                print("{:d}".format(value), end='')
                i = 0
            else:
                print("{:d}".format(value), end=' ')
        print()
