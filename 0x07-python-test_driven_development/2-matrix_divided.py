#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_list = []
    error_type = "matrix must be a matrix (list of lists) of integers/floats"
    error_size = "Each row of the matrix must have the same size"
    if type(matrix) is not list:
        raise TypeError(error_type)

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            new_list.append(matrix[y] / div)
