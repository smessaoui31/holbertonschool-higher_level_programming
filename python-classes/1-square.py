#!usr/bin/python3
"""
This module defines a class Square.

It creates square objects with a private size attribute.
"""


class Square:
    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
