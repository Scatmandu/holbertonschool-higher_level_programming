#!/usr/bin/python3
"""subclass Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass Square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """returns string representation of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
