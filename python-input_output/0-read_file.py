#!/usr/bin/python3
"""Function to open , read and close a file"""


def read_file(filename=""):
    with open('', encoding="utf-8") as f:
        print(f.read(), end="")
