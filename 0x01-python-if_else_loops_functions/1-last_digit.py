#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
last_neg = (number * -1) % 10
less_six = "and is less than 6 and not 0"
greater_five = "and is greater than 5"
if number >= 0:
    if last > 5:
        print('Last digit of {} is {} {}'.format(number, last, greater_five))
    if last == 0:
        print('Last digit of {} is {} and is 0'.format(number, last))
    if last < 6 and last > 0:
        print('Last digit of {} is {} {}'.format(number, last, less_six))
elif number < 0:
    print('Last digit of {} is -{} {}'.format(number, last_neg, less_six))
