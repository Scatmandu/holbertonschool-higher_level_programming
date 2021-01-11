#!/usr/bin/python3
"""class that defines Rectangle"""


class Square:
    """
    class Rectangle that contains the attributes width and height


    Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        assigns values height and width to class Rectangle


        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
    @property
    def width(self):
        """
        retrieves width from Rectangle class


        Returns:
            int: the value of width
        """
        return self.__width

    @width.setter
    def width(self, width=0):
        """
        sets the width of class Rectangle if it's a valid number


        Args:
            width (int): the width of the rectangle
        """
    @property
    def height(self):
        """
        retrieves height from Rectangle class


        Returns:
            int: the value of height
        """
    @height.setter
    def height(self, height=0):
        """
        sets the height of class Rectangle if it's a valid number


        Args:
            height (int): the height of the rectangle
        """
    if type(width) is not int:
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")
    if type(height) is not int:
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
