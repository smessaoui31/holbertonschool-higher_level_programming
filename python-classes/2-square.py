#!/usr/bin/python3
"""
This module defines a class Square.

It creates square objects with a private size attribute
and ensures the size is a non-negative integer.
"""


class Square:
    """
    This class represents a square.

    It stores the size of the square as a private attribute and
    ensures the value is an integer greater than or equal to 0.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of one side of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
