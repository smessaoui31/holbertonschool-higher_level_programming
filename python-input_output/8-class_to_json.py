#!/usr/bin/python3
"""
Returns dictionary description for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary of a simple object's attributes.
    """
    return obj.__dict__
