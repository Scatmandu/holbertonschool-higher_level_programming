#!/usr/bin/python3
"""prints a list of numbers separated by ", " """


for x in range(0, 100):
    if x != 99:
        print("{:02d}, ".format(x), end='')
    else:
        print(x)
