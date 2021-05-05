#!/usr/bin/python3
"""creates a rectangle class with a height and width"""


class Rectangle:
    """
    rectangle class that holds width and height

    Attributes:
        __height (integer):the height of the rectangle
        __width (integer): the width of the rectangle

    """
    def __init__(self, height):
        """
        Initializes a rectangle's height

        Args:
            height: the height of the new rectangle instance

        """
    def __init__(self, width):
        """
        Initializes a rectangle's height

        Args:
            height: the size of the new square instance

        """

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter for height"""

    if isinstance(height, int) is True:
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("height must be >= 0")
    else:
        raise TypeError("height must be an integer")

    @property
    def width(self):
        """getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter for width"""
        if isinstance(width, int) is True:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
