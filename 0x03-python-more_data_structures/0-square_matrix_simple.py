#!/usr/bin/python3
"""computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new_matrix.append(list(map(lambda num: num ** 2, x)))
    return (new_matrix)
