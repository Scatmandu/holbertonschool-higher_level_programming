#!/usr/bin/python3
"""reads a file and prints it to stdout"""


def read_file(filename=""):
    """uses with to read a file and print it to stdout"""

    with open(filename) as f:
        for line in f:
            print(line, end='')
