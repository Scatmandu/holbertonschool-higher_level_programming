#!/usr/bin/python3
"""creates the subclass Square from baseclass Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """sublass Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes square subclass"""
        super().__init__(size, size, x, y, id)

    def area(self):
        """calculates the area of the square"""
        return self.height * self.width

    def display(self):
        """print instance of square using #"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for w in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """prints string representation of square instance"""
        return ('[Square] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """assigns args to each attribute"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            if i == 1:
                self.width = args[1]
            if i == 2:
                self.height = args[2]
            if i == 3:
                self.x = args[3]
            if i == 4:
                self.y = args[4]

    @property
    def width(self):
        """returns private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """returns private instance attribute height"""
        return self.__height

    @property
    def x(self):
        """returns private instance attribute x"""
        return self.__x

    @property
    def y(self):
        """returns private instance attribute y"""
        return self.__y

    @width.setter
    def width(self, width):
        """sets width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """sets height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """sets x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """sets y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
