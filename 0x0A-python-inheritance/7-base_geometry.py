#!/usr/bin/python3
"""class BaseGeometry with method for area"""


class BaseGeometry:
    """class BaseGeometry with method for area"""
    def area(self):
        """empty method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates whether value is an int"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
