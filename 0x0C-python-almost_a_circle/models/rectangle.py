#!/usr/bin/python3
"""subclass of Base, Rectangle"""


from models.base import Base


class Rectangle(Base):
    """subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height_width_validator("width", width)
        self.__width = width
        self.height_width_validator("height", height)
        self.__height = height
        self.x_y_validator("x", x)
        self.__x = x
        self.x_y_validator("y", y)
        self.__y = y

    def area(self):
        """returns area of Rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints Rectangle using # in a position based on x y"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for w in range(self.__width):
                if w == 0:
                    for x in range(self.__x):
                        print(" ", end='')
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """assigns arguments to each attribute of Rectangle"""
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]

    def __str__(self):
        """returns string representation of Rectangle"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return "[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h)

    def to_dictionary(self):
        """returns dictionary representation of Rectangle"""
        d = {'x': self.x, 'y': self.y, 'id': self.id,
             'height': self.height, 'width': self.width}
        return d

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.height_width_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height setter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.height_width_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.x_y_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.x_y_validator("y", value)
        self.__y = value
