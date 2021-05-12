#!/usr/bin/python3
"""appends string to end of file and returns string's length"""


def append_write(filename="", text=""):
    """appends str to EOF and returns str's length"""

    count = 0

    with open(filename, "a") as f:
        f.write(text)
    for char in text:
        count += 1
    return count
