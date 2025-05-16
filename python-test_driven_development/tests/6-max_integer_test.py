#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -3, -1]), -1)

    def test_all_same(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed_int_and_float(self):
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_string_argument(self):
        self.assertEqual(max_integer("abc"), "c")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == '__main__':
    unittest.main()