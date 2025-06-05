#!/usr/bin/python3
"""
Module to convert a JSON string into a Python object.
"""


def from_json_string(my_str):
    """
    Convert JSON string to Python object.
    """
    import json
    return json.loads(my_str)
