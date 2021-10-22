#!/usr/bin/python3
"""class Base"""


import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def height_width_validator(self, name, value):
        """validates height/width values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def x_y_validator(self, name, value):
        """validates x/y values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """makes a list of dicts into a json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """makes list_objs into json and writes it to a file"""
        filename = cls.__name__ + '.json'
        newlist = []
        if not list_objs:
            list_objs = []
        for x in list_objs:
            newlist.append(x.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """makes json string into a dict"""
        if json_string is None or 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """sets all attributes of and returns a class"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1, 0, 0)

        if cls.__name__ == "Square":
            new_instance = cls(1, 0, 0)

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """returns a lsit of instances based on class"""
        filename = cls.__name__ + '.json'
        newList = []
        try:
            with open(filename, 'r') as f:
                newList = cls.from_json_string(f.read())
                for i, j in enumerate(newList):
                    newList[i] = cls.create(**newList[i])
            return newList
        except:
            return []
