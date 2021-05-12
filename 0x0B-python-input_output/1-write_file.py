#!/usr/bin/python3
"""writes a string to a txt file and returns number of characters"""


def write_file(filename="", text=""):
    """writes string to txtfile and returns number of chars"""

    count = 0

    with open(filename, "w") as f:
        f.write(text)
    for char in text:
        count += 1
    return count
