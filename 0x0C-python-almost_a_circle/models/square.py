#!/usr/bin/python3
"""subclass Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initiation based on Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string representaton of Square"""
        i = self.id
        x = self.x
        y = self.y
        s = self.width
        return "[Square] ({}) {}/{} - {}".format(i, x, y, s)

    def to_dictionary(self):
        """returns dictionary representation of Square"""
        d = {'id': self.id, 'x': self.x, 'size': self.width,
             'y': self.y}
        return d

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height_width_validator("width", value)
        self.width = value
        self.height = value
