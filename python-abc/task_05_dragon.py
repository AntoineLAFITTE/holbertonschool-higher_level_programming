#!/usr/bin/env/python3
"""This module demonstrates the use of mixins with the Dragon class."""


class SwimMixin:
    """A mixin that adds swimming capability to a class."""

    def swim(self):
        """Makes the creature swim."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that adds flying capability to a class."""

    def fly(self):
        """Makes the creature fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ A class representig a Dragon that can both swim and fly, inheriting
    from SwimMixin and FlyMixin.
    """

    def roar(self):
        """Makes the dragon roar."""
        print("The dragon roars!")
