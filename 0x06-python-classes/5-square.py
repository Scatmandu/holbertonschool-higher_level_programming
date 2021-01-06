#!/usr/bin/python3
"""creates class Square of int size and makes sure size >= 0"""


class Square:
    """
    class Square that contains the value size


    Attributes:
        __size (int): the size of the square


    """
    def __init__(self, size=0):
        """
        assigns size value to class Square


        Args:
            size (int): the size of the square


        """
        self.size = size

    def area(self):
        """
        returns the area based on the size of the class Square


        Returns:
            int: the result of size ** 2


        """
        result = (self.__size ** 2)
        return result

    def my_print(self):
        """prints a square using #"""
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end='')
            print()

    @property
    def size(self):
        """
        retrieves size from Square class


        Returns:
            int: the value of size


        """
        return self.__size

    @size.setter
    def size(self, size=0):
        """
        sets the size of class Square if it is a valid number


        Args:
            size (int): the size of the square


        """

        if isinstance(size, int) is True:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
