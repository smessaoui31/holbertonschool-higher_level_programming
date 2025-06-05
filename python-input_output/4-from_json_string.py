#!/usr/bin/python3
"""
Converts a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object from a JSON string.
    """
    return json.loads(my_str)
