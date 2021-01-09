#!/usr/bin/python3
"""module that contains text_indentation module"""


def text_indentation(text):
    """
    inserts two newlines after every . ? and : in a string


    Arguments:
        text (str): a string of chars
    """
    for x in text:
        if x == '.':
            print(x, end='')
            print("\n")
        elif x == '?':
            print(x, end='')
            print("\n")
        elif x == ':':
            print(x, end='')
            print("\n")
        else:
            print(x, end='')
