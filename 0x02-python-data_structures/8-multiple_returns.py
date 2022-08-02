#!/usr/bin/python3
"""returns a tuple with the length of a string and its first character"""


def multiple_returns(sentence):
    if sentence:
        tuppie = (len(sentence), sentence[0])
    else:
        tuppie = (len(sentence), None)
    return tuppie
