#!/usr/bin/python3
"""creating the class Base"""


import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes Base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return []
        else:
            f = json.dumps(list_dictionaries)
            return f
