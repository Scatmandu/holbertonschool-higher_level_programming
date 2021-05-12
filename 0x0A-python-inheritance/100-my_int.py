#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """does the opposite of what it should"""

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
