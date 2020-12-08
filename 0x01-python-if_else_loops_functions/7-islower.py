#!/usr/bin/python3
def islower(c):
    for x in range(97, 123):
        if ord(c) == x:
            return True
    if x == 123:
        return False
