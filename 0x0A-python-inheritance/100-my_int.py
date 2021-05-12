#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """does the opposite of what it should"""

    def __eq__(a, b):
        if a < b or a > b:
            return False
        else:
            return True

    def __ne__(a, b):
        if a < b or a > b:
            return True
        else:
            return False
