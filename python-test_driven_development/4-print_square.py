#!/usr/bin/python3
"""This module provides a function that prints a square with '#' characters."""


def print_square(size):
    """Prints a square of given size using '#'."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
