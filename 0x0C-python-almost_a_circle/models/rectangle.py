#!/usr/bin/python3
"""creates the subclass Rectangle from baseclass Base"""


from base.py import Base


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
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):

    @height.setter
    def height(self, height):

    @x.setter
    def x(self, x):

    @y.setter
    def y(self, y):
