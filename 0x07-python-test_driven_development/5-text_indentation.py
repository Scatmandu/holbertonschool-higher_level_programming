#!/usr/bin/python3
"""module that contains text_indentation module"""


def text_indentation(text):
    """
    inserts two newlines after every . ? and : in a string


    Arguments:
        text (str): a string of chars
    """
    for index, x in enumerate(text):
        if x == '.':
            print(x, end='')
            print("\n")
        elif x == '?':
            print(x, end='')
            print("\n")
        elif x == ':':
            print(x, end='')
            print("\n")
        elif x is ' ' and text[index - 1] is '.':
            pass
        elif x is ' ' and text[index - 1] is '?':
            pass
        elif x is ' ' and text[index - 1] is ':':
            pass
        else:
            print(x, end='')
