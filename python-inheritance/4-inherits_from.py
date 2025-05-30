#!/usr/bin/python3
"""
This module defines a function that checks
if an object inherits from a class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    Otherwise, returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance from.

    Returns:
        True if obj is an instance of a subclass of a_class
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
