#!/usr/bin/python3
"""inserts two newlines after each . ? and :"""


def text_indentation(text):
    """inserts two newlines after each . ? and :"""

    skip = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in text:
        if skip is True:
            skip = False
            continue
        if x == '.':
            print("{}\n".format(x))
            skip = True
        elif x == '?':
            print("{}\n".format(x))
            skip = True
        elif x == ':':
            print("{}\n".format(x))
            skip = True
        else:
            print(x, end="")
