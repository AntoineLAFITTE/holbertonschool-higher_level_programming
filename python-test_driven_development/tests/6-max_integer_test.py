#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittests for max_integer function"""

    def test_max_at_end(self):
        """Test list with max integer at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_in_middle(self):
        """Test list with max integer in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test list with only one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_integers(self):
        """Test list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test list with both positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_same_value(self):
        """Test list where all values are the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_at_start(self):
        """Test list with max integer at the start"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_float_in_list(self):
        """Test list with float numbers"""
        self.assertEqual(max_integer([1.5, 2.8, 3.7, 4.1]), 4.1)

    def test_mixed_data_types(self):
        """Test list with both integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.7]), 4.7)

    def test_string_in_list(self):
        """Test list with strings (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])


if __name__ == "__main__":
    unittest.main()
