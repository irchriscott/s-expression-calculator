import unittest
from calc import SExpressionCalculator

class SExpressionCalculatorTestCase(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual(SExpressionCalculator("0").calculate(), 0)
        self.assertEqual(SExpressionCalculator("123").calculate(), 123)

    def test_add_function(self):
        self.assertEqual(SExpressionCalculator("(add 1 1)").calculate(), 2)
        self.assertEqual(SExpressionCalculator("(add 0 (add 3 4))").calculate(), 7)
        self.assertEqual(SExpressionCalculator("(add 3 (add (add 3 3) 3))").calculate(), 12)

    def test_multiply_function(self):
        self.assertEqual(SExpressionCalculator("(multiply 1 1)").calculate(), 1)
        self.assertEqual(SExpressionCalculator("(multiply 0 (multiply 3 4))").calculate(), 0)
        self.assertEqual(SExpressionCalculator("(multiply 2 (multiply 3 4))").calculate(), 24)
        self.assertEqual(SExpressionCalculator("(multiply 3 (multiply (multiply 3 3) 3))").calculate(), 81)

    def test_mixed_functions(self):
        self.assertEqual(SExpressionCalculator("(add 1 (multiply 2 3))").calculate(), 7)
        self.assertEqual(SExpressionCalculator("(multiply 2 (add (multiply 2 3) 8))").calculate(), 28)

    def test_others_functions(self):
        self.assertEqual(SExpressionCalculator("(exponent 2 5)").calculate(), 32)
        self.assertEqual(SExpressionCalculator("(add 1 2 3 4 (multiply 2 3 5))").calculate(), 40)

if __name__ == '__main__':
    unittest.main()