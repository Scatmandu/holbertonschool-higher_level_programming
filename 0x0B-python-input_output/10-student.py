#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        strang = {}

        if attrs is not None:
            for key in attrs:
                if key in self.__dict__:
                    strang[key] = self.__dict__[key]
            return strang
        else:
            return vars(self)
