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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """sets height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """sets x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """sets y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
