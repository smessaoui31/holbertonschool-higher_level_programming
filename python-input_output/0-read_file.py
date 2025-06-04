#!/usr/bin/python3
"""Function to open , read and close a file"""


def read_file(filename=""):
    """
    Read a text file with utf-8
    filename = the name of the file to read

    Usage example:
    >>> read_file("tests/sample.txt")
    Hello, Holberton!
    """
    with open('', encoding="utf-8") as f:
        print(f.read(), end="")
