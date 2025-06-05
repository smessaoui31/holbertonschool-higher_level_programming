#!/usr/bin/python3
"""
This module handles reading from and writing to UTF-8 text files.
"""


def write_file(filename="", text=""):
    """
Write a string to a UTF-8 text file and returns
the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
