#!/usr/bin/python3
"""prints only the first occurrence of each number 0-100"""


for x in range(10):
    for y in range(10):
        if y > x:
            if (x != 8 or y != 9):
                print("{}{}".format(x, y), end=', ')
            else:
                print("{}{}".format(x, y))
