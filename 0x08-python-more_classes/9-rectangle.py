#!/usr/bin/python3
"""creates a rectangle class with a height and width"""


class Rectangle:
    """rectangle class that holds width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):

        return self.__width

    @height.setter
    def height(self, height):
        if isinstance(height, int) is True:
            if height >= 0:
                self.__height = height
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @width.setter
    def width(self, width):
        if isinstance(width, int) is True:
            if width >= 0:
                self.__width = width
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """returns the area of the rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.height is 0 or self.width is 0:
            return 0
        return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        """prints a rectangle using #"""
        string = ""
        if self.perimeter() == 0:
            return string
        else:
            for i in range(self.height):
                for i in range(self.width):
                    string += "#"
                string += "\n"
        return string[:-1]

    def __repr__(self):
        """
            returns a representation of the rectangle that
             can be used with eval() to duplicate it
        """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """This is for deleting the rectangle"""
        Rectangle.number_of_instances -= -1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """finds bigger rectangle based on area"""
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_2.area()) > (rect_1.area()):
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """creates an instance of a square rectangle"""
        return cls(size, size)
