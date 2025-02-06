#!/usr/bin/python3
"""CountedIterator class"""


class CountedIterator:
    """Class of CountedIterator """
    counter = 0
    item = []
    iterator = ""

    def __init__(self, item):
        """constructor for CountedIterator"""
        # self.item = item
        self.iterator = iter(item)

    def get_count(self):
        """method get_count to return counter value"""
        return self.counter

    # def next(self, iterator):
    def __next__(self):
        """method next that return next item of an iterator.
        __next__ as it built inn method """
        self.counter += 1
        return (next(self.iterator))
