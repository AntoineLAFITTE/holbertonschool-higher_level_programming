#!/usr/bin/env/python3
"""This module demonstrates multiple inheritance with the FlyingFish class."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Method to make the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """Method to describle the fish habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""
    def fly(self):
        """Method to make the bird fly."""
        print("The bird is flying")

    def habitat(self):
        """Method to describle the fish habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish that inherits
    from both Fish and Bird classes
    """

    def swim(self):
        """Override swim method for flyingfish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method for flyingfish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override fly method for flyingfish"""
        print("The flying fish lives both in water and the sky!")


# Testing the FlyingFish class
if __name__ == "__main__":
    flying_fish = FlyingFish()

    # Test methods
    flying_fish.swim()    # Should print "The flying fish is swimming!"
    flying_fish.fly()     # Should print "The flying fish is soaring!"
    flying_fish.habitat()  # "The flying fish lives both in water and the sky!"

    # Investigate the method resolution order (MRO)
    print(FlyingFish.mro())
