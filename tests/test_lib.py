# This file exports testing functions for the mathematics library
# Author: Refaat || Version: 2.0
import unittest
import sys

sys.path.append("./src/mathematics")

from lib import *

class TestMathetmaticsLibrary(unittest.TestCase):
    #### Version 1.0 tests ####
    def test_add(self):
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(2,1), 3)
        self.assertEqual(add(1,2), 3)

    def test_subtract(self):
        self.assertEqual(substract(2,2),  0)
        self.assertEqual(substract(2,1),  1)
        self.assertEqual(substract(1,2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2,2),    4)
        self.assertEqual(multiply(2,1),    2)
        self.assertEqual(multiply(1,2),    2)
        self.assertEqual(multiply(-1,2),  -2)
        self.assertEqual(multiply(-1,-2),  2)

    def test_divide(self):
        self.assertEqual(divide(2,2),    1)
        self.assertEqual(divide(2,1),    2)
        self.assertEqual(divide(1,2),    0.5)
        self.assertEqual(divide(-1,2),  -0.5)
        self.assertEqual(divide(-1,-2),  0.5)
        
        with self.assertRaises(ZeroDivisionError):
            divide(1/0)

    #### Version 2.0 tests ####
    def test_slope(self):
        self.assertEqual(slope(3,2,9,4), 5)
        self.assertEqual(slope(-12,6,4,-6), -5/9)
        self.assertEqual(slope(7,7,2,2), None)


if __name__ == '__main__':
    unittest.main()
