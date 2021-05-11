#!/usr/bin/python3
"""write a class that inherits from list"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
            print(sorted(self))
