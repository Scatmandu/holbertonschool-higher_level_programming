#!/usr/bin/python3
"""class BaseGeometry with method for area"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.__width = BaseGeometry().integer_validator("width", width)
        self.__height = BaseGeometry().integer_validator("height", height)
