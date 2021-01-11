import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_and_beginning_max(self):
        list = [4, 2, 3, 1]
        self.assertEqual(max_integer(list), 4)

    def test_all_negative(self):
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)

    def test_empty(self):
        list = []
        self.assertEqual(max_integer(list), None)

    def test_end_max(self):
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_middle_max(self):
        list = [1, 2, 4, 3]
        self.assertEqual(max_integer(list), 4)

    def test_one_negative(self):
        list = [2, 1, 0, -1]
        self.assertEqual(max_integer(list), 2)

    def test_one_element(self):
        list = [1]
        self.assertEqual(max_integer(list), 1)

if __name__ == '__main__':
    unittest.main()
