#!/usr/bin/python3
"""writes a string to a text file and returns # of chars written"""


def write_file(filename="", text=""):
    """Writes and counts the characters of a string"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
