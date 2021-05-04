#!/usr/bin/python3
"""creates class square with a size"""


class Square:
    """
    square class that holds size

    Attributes:
        __size (integer): the size of the square instance

    """
    def __init__(self, size):
        """
        Initializes a square of size size

        Args:
            size: the size of the new square instance

        """
        self.__size = size
