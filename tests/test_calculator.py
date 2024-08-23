import pytest

from src.calculator import Calculator 

class TestCalculator:
    def test_calculator_plus(self):
        result = Calculator.plus(3, -6)
        expected = -3

        assert result == expected

    def test_calculator_subtract(self):
        result = Calculator.subtract(3, -6)
        expected = 9

        assert result == expected

    def test_calculator_product(self):
        result = Calculator.product(3, -6)
        expected = -18

        assert result == expected

    def test_calculator_quotient(self):
        result = Calculator.product(3, -6)
        expected = -18

        assert result == expected