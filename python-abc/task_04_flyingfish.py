#!/usr/bin/env python3
"""
Demonstrates multiple inheritance with FlyingFish.
"""


class Fish:
    """Fish class with basic behavior."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Bird class with basic behavior."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish with overridden methods from Fish and Bird."""

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
