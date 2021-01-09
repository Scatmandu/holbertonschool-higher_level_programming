#!/usr/bin/python3
"""divides a 2d list by div"""
def matrix_divided(matrix, div):

    new_matrix = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix.append(round(int(j) / div, 2))
    return new_matrix
