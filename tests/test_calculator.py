### TDD - Test Driven Development + cykl Red Green Refactor
# 1. Red - czerwony test - napisałem go ale nie przechodzi bo kod nie działa :-(
# 2. Green - zielony, przechodzący test - napisałem kod, który "zadowolił test" nawet, jeśli kod jest szpetny
# 3. Refactor - mając test, co do którego wiem, że sprawdza to na czym mi zależy zaczynam eksperymentować z kodem żeby go poprawić

from unittest import TestCase
from calculator import calculate, Calculation


class TestCalculate(TestCase):
    def test_calculate_addition(self):
        self.assertEqual(10, calculate(Calculation.add, 3, 7))

    def test_calculate_subtraction(self):
        self.assertEqual(0, calculate(Calculation.subtract, 7, 7))
        self.assertEqual(3, calculate(Calculation.subtract, 10, 7))
        self.assertEqual(-5, calculate(Calculation.subtract, 15, 20))

    def test_calculate_multiplication(self):
        self.assertEqual(25, calculate(Calculation.multiply, 5, 5))
        self.assertEqual(42, calculate(Calculation.multiply, 6, 7))
        self.assertEqual(24, calculate(Calculation.multiply, 8, 3))

    def test_calculate_division(self):
        self.assertEqual(2, calculate(Calculation.divide, 4, 2))
        self.assertEqual(7, calculate(Calculation.divide, 14, 2))
