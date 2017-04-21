import math

from calculator.calculator_interface import ICalculator


class CalculatorFunctions(ICalculator):
    """Calculator interface implementation"""

    __history = []

    def get_history(self):
        return self.__history

    def add(self, var):
        output = 0
        i = 0
        while i < len(var):
            output += var[i]
            i += 1
        self.__history.append(["Add", var, output])
        return output

    def multiply(self, var):
        output = 1
        i = 0
        while i < len(var):
            output = int(output) * int(var[i])
            i = i + 1
        self.__history.append(["Multiply", var, output])
        return output

    def pow(self, var):
        output = var ** 2
        self.__history.append(["Square", var, output])
        return output

    def square_root(self, var):
        output = math.sqrt(var)
        self.__history.append(["Square root", var, output])
        return output
