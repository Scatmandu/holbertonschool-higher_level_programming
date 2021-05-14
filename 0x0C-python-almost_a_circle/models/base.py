#!/usr/bin/python3
"""creating the class Base"""


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes Base instance"""

        if id is not None:
            self.id = id
        elif type(id) is not int:
            raise TypeError("id must be an integer")
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
