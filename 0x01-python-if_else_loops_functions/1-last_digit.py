#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {} is ".format(number), end='')
if number > 0:
    last_digit = number % 10
else:
    last_digit = number % -10
if last_digit > 5:
    print(last_digit, end='')
    print(" and is greater than 5".format(number, last_digit))
elif last_digit == 0:
    print(last_digit, end='')
    print(" and is 0".format(number, last_digit))
else:
    print(last_digit, end='')
    print(" and is less than 6 and not 0".format(number, last_digit))
