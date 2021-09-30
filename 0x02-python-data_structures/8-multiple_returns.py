#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        tuppie = (len(sentence), sentence[0])
    else:
        tuppie = (len(sentence), None)
    return tuppie
