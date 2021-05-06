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
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @width.setter
    def width(self, width):
        if isinstance(width, int) is True:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """returns the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.height is 0 or self.width is 0:
            return 0
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """prints a rectangle using #"""
        string = ""
        if self.perimeter() == 0:
            return string
        else:
            for i in range(self.height):
                for i in range(self.width):
                    string += "#"
                string += "\n"
        return string[:-1]

    def __repr__(self):
        """
            returns a representation of the rectangle that
             can be used with eval() to duplicate it
        """
        return ("Rectangle({}, {})".format(self.width, self.height))
