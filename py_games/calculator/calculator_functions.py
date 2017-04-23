import math

from py_games.calculator import ICalculator


class CalculatorFunctions(ICalculator):
    """Calculator interface implementation"""

    @staticmethod
    def add(var):
        output = 0
        i = 0
        while i < len(var):
            output += var[i]
            i += 1
        return output

    @staticmethod
    def multiply(var):
        output = 1
        i = 0
        while i < len(var):
            output = int(output) * int(var[i])
            i = i + 1
        return output

    @staticmethod
    def pow(var):
        return var ** 2

    @staticmethod
    def square_root(var):
        return math.sqrt(var)
