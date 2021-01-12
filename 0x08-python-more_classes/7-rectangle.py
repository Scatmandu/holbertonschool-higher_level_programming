#!/usr/bin/python3
"""class that defines Rectangle"""


class Rectangle:
    """
    class Rectangle that contains the attributes width and height


    Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
        number_of_instances (int): count for instances of Rectangle
        print_symbol (): used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        assigns values height and width to class Rectangle


        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        converts our Rectangle into a string


        Returns:
            our Rectangle represented by #'s
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                    string += str(self.print_symbol)
            string += '\n'
        return string

    def __repr__(self):
        """returns a printable representation of the object"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """notifies when the garbage collector deletes Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """
        calculates the area of a rectangle


        Returns:
            the result of width * height
        """
        result = self.__width * self.__height
        if self.__width == 0 or self.__height == 0:
            result = 0
        return result

    def perimeter(self):
        """
        calculates the perimeter of a rectangle


        Returns:
            the result of (2 * height) + (2 * width)
        """
        result = ((2 * self.__height) + (2 * self.__width))
        return result

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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        retrieves height from Rectangle class


        Returns:
            int: the value of height
        """
        return self.__height

    @height.setter
    def height(self, height=0):
        """
        sets the height of class Rectangle if it's a valid number


        Args:
            height (int): the height of the rectangle
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
