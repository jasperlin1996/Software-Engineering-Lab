from Calculator import *
import unittest

class TestCalculator(unittest.TestCase):
    def test_int1_add(self):
        self.assertEqual(add(9, 3), 12)

    def test_int2_add(self):
        self.assertEqual(add(9, 4), 13)

    def test_float1_add(self):
        self.assertEqual(add(4.2, 3), 7.2)

    def test_int1_minus(self):
        self.assertEqual(minus(9, 3), 6)

    def test_int2_minus(self):
        self.assertEqual(minus(9, 4), 5)

    def test_float1_minus(self):
        self.assertEqual(minus(4.2, 3.2), 1.0)

    def test_int1_times(self):
        self.assertEqual(times(9, 3), 27)

if __name__ == '__main__':
    unittest.main()
