#!/usr/bin/bash
def raise_exception_msg(message=""):
    try:
        raise NameError
    except NameError:
        print(message)
