#!/usr/bin/python3
"""this module has one method that prints a first name and last name"""


def say_my_name(first_name, last_name=""):
    """
    ``say_my_name`` - prints first name and last name


    Arguments:
        first_name - a first name
        last_name - a last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
