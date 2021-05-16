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
        return ('[Square] ({}) {}/{} - {}'
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assigns args to each attribute"""
        if len(args) is not 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns dictionary representation of square"""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size
