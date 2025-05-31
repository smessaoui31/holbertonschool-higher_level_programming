#!/usr/bin/env python3
"""
Implements a Dragon class using mixins for flying and swimming.
"""


class SwimMixin:
    """Mixin that adds swimming capability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly."""

    def roar(self):
        print("The dragon roars!")
