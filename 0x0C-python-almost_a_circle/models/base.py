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
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string rep of json_string"""
        if json_string is None:
            return []
        else:
            return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation to a file"""
        filename = "{}.json".format(cls.__name__)
        json_rep = []
        if list_objs is not None:
            for objects in list_objs:
                json_rep.append(cls.to_dictionary(objects))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(json_rep))
