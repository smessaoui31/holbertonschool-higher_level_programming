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
    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
