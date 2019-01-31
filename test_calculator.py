"""
Unit tests for calculator library
"""

import calculator


class TestCalc:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.subtract(4, 2)
