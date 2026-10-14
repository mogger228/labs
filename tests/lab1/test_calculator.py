import unittest

from src.lab1.calculator import calculate


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtract(self):
        self.assertEqual(calculate(5, 3, "-"), 2)

    def test_multiply(self):
        self.assertEqual(calculate(4, 3, "*"), 12)

    def test_divide(self):
        self.assertEqual(calculate(10, 4, "/"), 2.5)

    def test_power(self):
        self.assertEqual(calculate(2, 10, "^"), 1024)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(1, 0, "/")

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculate(1, 2, "%")


if __name__ == "__main__":
    unittest.main()
