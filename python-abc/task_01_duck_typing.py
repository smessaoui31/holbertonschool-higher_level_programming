#!/usr/bin/env python3
"""
Defines abstract Shape class and concrete Circle and Rectangle classes.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the shape's area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the shape's perimeter."""
        pass


class Circle(Shape):
    """Concrete Circle class implementing Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete Rectangle class implementing Shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of any shape implementing the Shape interface.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
