#!/usr/bin/python3
"""creates a rectangle class with a height and width"""


class Rectangle:
    """rectangle class that holds width and height"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):

        return self.__width

    @height.setter
    def height(self, height):
        if isinstance(height, int) is True:
            if height <= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @width.setter
    def width(self, width):
        if isinstance(width, int) is True:
            if width <= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
