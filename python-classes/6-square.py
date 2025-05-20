#!/usr/bin/python3
"""
This module defines a class Square.

It creates square objects with a private size and position,
validates inputs, and provides methods to calculate area
and print the square with correct positioning.
"""


class Square:
    """
    This class represents a square.

    It stores the size and position as private attributes and
    provides methods to calculate area and print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): Tuple of 2 non-negative integers.
        """
        self.size = size
        self.position = position

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
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a valid tuple of 2 non-negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters, considering position.

        If size is 0, prints an empty line.
        Applies vertical and horizontal spacing based on position.
        """
        if self.__size == 0:
            print()
            return

        # Vertical spacing
        for _ in range(self.__position[1]):
            print()

        # Square lines with horizontal spacing
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
