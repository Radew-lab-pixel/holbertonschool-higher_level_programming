#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def setUp(self):
        self.testListNone = None


    # def test_type(self):

    #    with self.assertRaises(AssertionError):
    #        max_integer([])
    
    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_begin(self):
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_one_neg(self):
        self.assertEqual(max_integer([1, 2, 3, -4, 5]), 5)
    
    def test_max_all_neg(self):
        self.assertEqual(max_integer([-2, -6, -1, -3, -5]), -1)

    def test_max_only_one(self):
        self.assertEqual(max_integer([3]), 3)

    def test_max_none(self):
        # self.assertEqual(max_integer(), 0)
        # with self.assertRaises(AssertionError):
            # max_integer()
            # self.testListNone[:1]
            # self.assertEqual("'NoneType' object is not subscriptable", str(err.exception))
        self.assertEqual(max_integer(), None)