#!/usr/bin/python3
"""
Defines a Rectangle class inheriting from BaseGeometry with validated dimensions.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class to represent a rectangle, with validation of dimensions."""

    def __init__(self, width, height):
        """Initialize a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
