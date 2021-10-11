#!/usr/bin/python3
"""prints two newlines after certain characters in text"""


def text_indentation(text):
    """prints two newlines after certain characters in text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in text:
        if x == ' ' and remove_space is True:
            continue
        elif x == '.' or x == '?' or x == ':':
            print("{}\n".format(x))
            remove_space = True
        else:
            print(x, end="")
            remove_space = False
