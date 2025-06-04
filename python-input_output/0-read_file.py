#!/usr/bin/python3
"""
This module provides a function to read and
print the contents of a UTF-8 text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Usage example:
    >>> read_file("tests/sample.txt")
    Hello, Holberton!
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
