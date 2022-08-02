#!/usr/bin/python3
"""checks if a number is positive, ngative, or 0"""


import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negative".format(number))
