#!/usr/bin/env python3
"""This module defines a VerboseList class that extends the built-in list class
with notifications."""


class VerboseList(list):
    """A subclass of list that prints notifications
    when items are added or removed."""

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with items from an iterable
        and prints a notification."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Removes the first occurrence of an item from the list
        and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Removes and returns the item at the given index or the last item
        if no index is provided. Prints a notification."""
        item = self[index]  # Get the item before removing it
        super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
