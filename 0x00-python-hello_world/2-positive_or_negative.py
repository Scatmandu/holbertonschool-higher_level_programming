#!/usr/bin/python3
"""checks whether a number is positive, negative, or zero"""


import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number))
if number == 0:
    print("{:d} is zero".format(number))
if number < 0:
    print("{:d} is negative".format(number))
