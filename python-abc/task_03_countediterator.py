#!/usr/bin/env/pyhon3
"""This module defines a CountedIterator that extends the behavior
of an iterator by counting the items iterated."""


class CountedIterator:
    """A custom iterator that counts how many items have been iterated over"""

    def __init__(self, iterable):
        """Initializes the CountedIterator with an iterable and a counter."""
        self.iterator = iter(iterable)  # Makes the iterable an iterator
        self.count = 0  # counter initialized at 0

    def __next__(self):
        """Fetches the next item and increments the counter.

        Raises:
            StopIteration: If there are no more items in the iterator.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            # If there are no more items raise Stop Iteration to signal the end
            raise StopIteration

    def get_count(self):
        """Returns the current count of items that have been iterated over."""
        return self.count
