import math
from pprint import pprint
from time import strftime, gmtime

from calculator.calculator_interface import ICalculator


class MyCalculator(ICalculator):
    """Calculator interface implementation"""

    __history = []

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

    def run(self):
        while True:
            choice = str(input("What do you want to do?: m/a/pow/sqrt/history/X: m: \n") or 'm')
            if choice == 'm':
                var = [int(x) for x in input("Give multiplication: \n").split()]
                if var:
                    print(self.multiply(var))
            elif choice == 'a':
                var = [int(x) for x in input("Give addition: \n").split()]
                if var:
                    print(self.add(var))
            elif choice == 'pow':
                var = int(input("Give variable for power: \n"))
                if var:
                    print(self.pow(var))
            elif choice == 'sqrt':
                var = int(input("Give variable for square root: \n"))
                if var:
                    print(self.square_root(var))
            elif choice == 'X':
                break
            elif choice == 'history':
                pprint(self.__history)
            else:
                continue
