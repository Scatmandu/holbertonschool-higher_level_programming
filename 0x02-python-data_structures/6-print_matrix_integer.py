#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        for value in row:
            i += 1
            if i == len(row):
                print("{}".format(value), end='')
                i = 0
            else:
                print("{}".format(value), end=' ')
        print()
