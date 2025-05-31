#!/usr/bin/python3
class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")
