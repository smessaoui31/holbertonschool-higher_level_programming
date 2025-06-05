#!/usr/bin/python3
"""
This module provides a function to append text to a
UTF-8 file and return the number of characters written.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.
    If the file does not exist, it will be created.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
