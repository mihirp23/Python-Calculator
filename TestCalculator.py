# Name : Mihir Patel
# Date : 6/27/19
# File : TestCalculator.py
# Perform unit tests on the calculate function from the calculator module.

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    ############################################################
    def testAddition(self):
    ############################################################
        self.assertEqual(calculator.calculate('+', 1, 2), 3)
        self.assertEqual(calculator.calculate('+', 1, -1), 0)
    # testAddition()

    ############################################################
    def testSubtraction(self):
    ############################################################
        self.assertEqual(calculator.calculate('-', 4, 1), 3)
        self.assertEqual(calculator.calculate('-', 1, -1), 2)
    # testSubtraction()

    ############################################################
    def testMultiplication(self):
    ############################################################
        self.assertEqual(calculator.calculate('*', 3, 9), 27)
        self.assertEqual(calculator.calculate('*', 8, -8), -64)
    # testMultiplication()

    ############################################################
    def testDivision(self):
    ############################################################
        self.assertEqual(calculator.calculate('/', 9, 3), 3)
        self.assertEqual(calculator.calculate('/', 8, -2), -4)
        self.assertEqual(calculator.calculate('/', 8, 0), 'Undefined')
    # testDivision()

    ############################################################
    def testFactorial(self):
    ############################################################
        self.assertEqual(calculator.calculate('factorial', 5), 120)
    # testFactorial()

    ############################################################
    def testSqrt(self):
    ############################################################
        self.assertEqual(calculator.calculate('sqrt', 16), 4.0)
    # testSqrt()

    ############################################################
    def testPow(self):
    ############################################################
        self.assertEqual(calculator.calculate('^', 2, 3), 8)
    # testPow()

    ############################################################
    def testGcd(self):
    ############################################################
        self.assertEqual(calculator.calculate('gcd', 18, 6), 6)
    # testGcd()


if __name__ == "__main__":
    unittest.main()
