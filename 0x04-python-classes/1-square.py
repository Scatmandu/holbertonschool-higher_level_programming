#!/usr/bin/python3
"""create class name Square"""


class Square:
    """the square class"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
