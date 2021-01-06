#!/usr/bin/python3
"""creates class Square of int size and makes sure size >= 0"""


class Square:
    """
    class Square that contains the value size


    Attributes:
        __size (): the size of the square


    """
    def __init__(self, size=0):
        """
        assigns size value to class Square


        Args:
            size (): the size of the square


        """

        if isinstance(size, int) is True:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
