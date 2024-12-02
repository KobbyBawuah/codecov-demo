import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

    def test_power(self):
        self.assertEqual(Calculator.power(2, 3), 8)

    # Intentionally skipping tests for `modulo` and `factorial`.

    def test_square_root(self):
        self.assertEqual(Calculator.square_root(16), 4)
        with self.assertRaises(ValueError):
            Calculator.square_root(-4)

if __name__ == '__main__':
    unittest.main()
