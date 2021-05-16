#!/usr/bin/python3
"""inserts a string into a file after a certain string"""


def append_after(filename="", search_string="", new_string=""):
    """Append new strings"""
    new_list = []
    with open(filename, 'r+') as f:
        """Read to new string"""
        for line in f:
            new_list.append(line)
            if search_string in line:
                new_list.append(new_string)
    with open(filename, 'w+') as f:
        f.write("".join(new_list))
