#!/usr/bin/python3
"""
Loads a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
