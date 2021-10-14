#!/usr/bin/python3
"""appends str to end of file and returns # of chars appended"""


def append_write(filename="", text=""):
    """Appends str to end of file and returns # of chars appended"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
