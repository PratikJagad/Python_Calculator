import unittest
from Calculator import add, subtract, multiply, Division

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 3), -3)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_division(self):
        self.assertEqual(Division(6, 3), 2)
        self.assertAlmostEqual(Division(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            Division(5, 0)  # should raise an error

if __name__ == "__main__":
    unittest.main()