#!/usr/bin/env/python3
from abc import ABC, abstractmethod
"""imports ABC and abstractmethod from the abc module"""


class Animal(ABC):
    """Creates Animal class"""
    @abstractmethod
    def sound(self):
        """Creates the abstarct method sound"""
        pass

class Dog(Animal):
    """Creates Sublclass Dog of Animal class"""
    def sound(self):
        """Creates the method sound for Dog"""
        return "Bark"

class Cat(Animal):
    """Creates Subclass Cat of Animal class"""
    def sound(self):
        """Creates method sound for Cat"""
        return "Meow"
