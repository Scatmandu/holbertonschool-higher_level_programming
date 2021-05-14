#!/usr/bin/python3
"""creates the subclass Rectangle from baseclass Base"""


from models.base import Base


class Rectangle(Base):
    """sublass Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangle sublcass from Base"""

        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """returns private instance attribute height"""
        return self.__height

    @property
    def x(self):
        """returns private instance attribute x"""
        return self.__x

    @property
    def y(self):
        """returns private instance attribute y"""
        return self.__y

    @width.setter
    def width(self, width):
        """sets width"""
        self.__width = width

    @height.setter
    def height(self, height):
        """sets height"""
        self.__height = height

    @x.setter
    def x(self, x):
        """sets x"""
        self.__x = x

    @y.setter
    def y(self, y):
        """sets y"""
        self.__y = y
