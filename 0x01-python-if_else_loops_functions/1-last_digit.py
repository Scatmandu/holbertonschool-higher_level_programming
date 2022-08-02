#!/usr/bin/python3
"""captures last digit of a number and classifies it"""


import random
number = random.randint(-10000, 10000)
if number < 0:
        last_digit = (number * -1) % 10 * -1
else:
    last_digit = number % 10
s1 = "Last digit of"
s2 = "and is greater than 5"
s3 = "and is 0"
s4 = "and is less than 6 and not 0"
if last_digit > 5:
    print("{:s} {:d} is {:d} {:s}".format(s1, number, last_digit, s2))
if last_digit == 0:
    print("{:s} {:d} is {:d} {:s}".format(s1, number, last_digit, s3))
if (last_digit < 6 and last_digit != 0):
    print("{:s} {:d} is {:d} {:s}".format(s1, number, last_digit, s4))
