#!/usr/bin/python3
"""reads text file and prints it to stdout"""


def read_file(filename=""):
    """see above"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
