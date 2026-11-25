import unittest
from calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate("5 + 3"), 8)

    def test_subtract(self):
        self.assertEqual(calculate("10 - 4"), 6)

    def test_multiply(self):
        self.assertEqual(calculate("4 * 3"), 12)

    def test_divide(self):
        self.assertEqual(calculate("10 / 2"), 5)

    def test_power(self):
        self.assertEqual(calculate("2 ** 3"), 8)


if __name__ == "__main__":
    unittest.main()