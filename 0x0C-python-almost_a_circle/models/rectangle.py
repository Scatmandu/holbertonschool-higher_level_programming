#!/usr/bin/python3
"""creates the subclass Rectangle from baseclass Base"""


from models.base import Base


class Rectangle(Base):
    """sublass Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangle sublcass from Base"""

        super(Rectangle, self).__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """calculated the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """print instance of Rectangle using #"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for w in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """prints string representation of rectangle instance"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """assigns args to each attribute"""
        if len(args) is not 0:
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
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary representation of rectangle"""
        rec_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return rec_dict

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
