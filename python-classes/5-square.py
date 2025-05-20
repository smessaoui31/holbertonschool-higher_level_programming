#!/usr/bin/python3
"""
This module defines a class Square.

It creates square objects with a private size attribute
and includes methods to compute area and print the square.
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
        self.size = size  # Use the setter

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # ✅ assignation ajoutée

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The square of the size.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters.

        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
