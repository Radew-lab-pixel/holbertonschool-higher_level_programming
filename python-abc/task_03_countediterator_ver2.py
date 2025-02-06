#!/usr/bin/python3
"""CountedIterator class"""


# class CountedIterator(iter):
class CountedIterator(iter):
    """class CountedIterator inherits from iter"""
    counter = 0
    def __init__(self, item=[]):
        """constructor"""
        # self.item = item
        # super().__init__(self, item)
        # super().__init__(item)
        self.counter = 0
        self.item = item
        # Convert the list into an iterator
        # self.iterator = iter(item)
        # CountedIterator.counter += 1
        # self.counter += 1

    def get_count(self):
        """get_count method"""
        return self.counter

    def next(self):
        result = next(self.iterator)
        self.counter += 1
        return result





