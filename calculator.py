from enum import Enum


class Calculation(Enum):
    add = 1
    subtract = 2
    divide = 3
    multiply = 4


def calculate(calculation_type: Calculation, first_number: float, second_number: float):
    match calculation_type:
        case Calculation.add:
            return first_number + second_number
        case Calculation.subtract:
            return first_number - second_number
        case Calculation.multiply:
            return first_number * second_number
        case Calculation.divide:
            if second_number == 0:
                return None

            return first_number / second_number
