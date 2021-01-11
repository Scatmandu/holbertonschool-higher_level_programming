import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive(self):
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_negative(self):
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)

    def test_empty(self):
        list = []
        self.assertEqual(max_integer(list), None)

if __name__ == '__main__':
    unittest.main()
