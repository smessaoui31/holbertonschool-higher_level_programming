#!/usr/bin/env python3
"""
Defines CountedIterator class that tracks iteration count.
"""


class CountedIterator:
    """Custom iterator that counts how many items were iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items returned so far."""
        return self.count
