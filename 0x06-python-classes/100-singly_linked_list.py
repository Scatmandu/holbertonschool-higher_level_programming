#!/usr/bin/python3
"""creates class Node of a singly linked list"""


class Node:
    """
    class Node that contains the value data


    Attributes:
        __data (int): the data in the node
        __next_node (): the next node in the list


    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        retrieves data from Node class


        Returns:
            int: the value of size


        """
        return self.__data

    @data.setter
    def data(self, data=0):
        """
        sets the data of class Node if it is a valid number


        Args:
            data (int): data to store in list


        """

        if isinstance(data, int) is True:
            if data >= 0:
                self.__data = data
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
