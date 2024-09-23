#!/usr/bin/python3
""" MyList class wich inherits from list"""


class MyList(list):
    """Class MyList wich inherits from list class"""
    def __init__(self):
        """Initializes MyList object"""
        super().__init__()

    def print_sorted(self):
        """
        Prints the list, sorted in ascending order.
        """
        print(sorted(self))
