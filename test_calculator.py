"""
Unit tests for calculator library
"""

import calculator


class TestCalc:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 1 == calculator.divide(10, 10)
