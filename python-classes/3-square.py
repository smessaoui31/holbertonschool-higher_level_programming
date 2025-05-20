#!/usr/bin/python3
"""
This module defines a class Square.

It creates square objects with a private size attribute.
"""


class Square:
    """
    This class represents a square.

    It stores the size of the square as a private attribute.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The square of the size.
        """
        return self.__size ** 2
