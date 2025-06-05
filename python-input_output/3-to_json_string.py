#!/usr/bin/python3
"""
Module to convert a JSON string into a Python object.
"""
import json


def from_json_string(my_obj):
    """
    Convert JSON string to Python object.
    """
    return json.loads(my_obj)
