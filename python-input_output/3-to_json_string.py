#!/usr/bin/python3
"""
Converts a Python object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Convert JSON string to Python object.
    """
    return json.loads(my_obj)
