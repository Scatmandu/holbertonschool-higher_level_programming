#!/usr/bin/python3
"""prints a specific range of the alphabet"""


for x in range(97, 123):
    if x == 101 or x == 113:
        continue
    else:
        print("{:c}".format(x), end='')
