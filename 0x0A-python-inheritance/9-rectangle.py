#!/usr/bin/python3
"""class BaseGeometry with method for area"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        BaseGeometry().integer_validator("width", width)
        self.__width = width
        BaseGeometry().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """string representation of class Rectangle"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """calculates the area of a rectangle"""

        return self.__width * self.__height
