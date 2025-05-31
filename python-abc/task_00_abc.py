#!/usr/bin/env python3
"""
Defines an abstract Animal class with sound method.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Produce a sound characteristic of the animal."""
        pass


class Dog(Animal):
    """Dog class that implements the Animal sound."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements the Animal sound."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
