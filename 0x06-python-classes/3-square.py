#!/usr/bin/python3
"""creates class square with a size and makes sure size is an int and >= 0"""


class Square:
    """
    square class that holds size

    Attributes:
        __size (integer): the size of the square instance

    """
    def __init__(self, size=0):
        """
        Initializes a square of size size

        Args:
            size: the size of the new square instance

        """
        if isinstance(size, int) is True:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the area of the base square"""
        return (self.__size ** 2)
