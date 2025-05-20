#!usr/bin/python3
"""
This module defines a class Square.

It creates square objects with a private size attribute.
"""


class Square:
    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.size = size  # Use the setter

    @property
    def size(self):
        return self.__size  # Getter

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
