#!/usr/bin/python3
"""unittest for max_integer()"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):

    def test_ordered(self):
        self.assertEqual.(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        self.assertEqual.(max_integer([]), None)

    def test_negative(self):
        self.assertEqual.(max_integer([-1, -2, -3]), -1)

    def test_one(self):
        self.assertEqual.(max_integer([7]), 7)

    def test_unordered(self):
        self.assertEqual.(max_integer([4, 1, 7, 9]), 9)


if __name__ == "__main__":
    unittest.main()
