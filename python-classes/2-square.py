#!/usr/bin/python3
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
