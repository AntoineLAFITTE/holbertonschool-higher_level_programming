#!/usr/bin/python3
""" MyList class wich inherits from list"""


class MyList(list):
    """
    A class wich inherits from list and adds a method to print the list sorted
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
