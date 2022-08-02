#!/usr/bin/python3
""" prints all possible different combinations of two digits"""


for x in range(10):
    for y in range(10):
        if y > x:
            if (x != 8 or y != 9):
                print("{}{}".format(x, y), end=', ')
            else:
                print("{}{}".format(x, y))
