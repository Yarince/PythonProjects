from pprint import pprint

from py_games.calculator.calculator_functions import CalculatorFunctions


class MyCalculator:
    """Calculator interface implementation"""

    __history = []

    def __init__(self):
        self.__calc_func = CalculatorFunctions()

    def run(self):
        while True:
            choice = str(input("What do you want to do?: m/a/pow/sqrt/history/X: m: \n") or 'm')
            if choice == 'm':
                self.exec_multiply()
            elif choice == 'a':
                self.exec_add()
            elif choice == 'pow':
                self.exec_power()
            elif choice == 'sqrt':
                self.exec_sqrt()
            elif choice == 'X':
                break
            elif choice == 'history':
                pprint(self.__history)
            else:
                continue

    def exec_sqrt(self):
        var = int(input("Give variable for square root: \n"))
        if var:
            output = self.__calc_func.square_root(var)
            self.__history.append(["Add", var, output])
            print(output)

    def exec_power(self):
        var = int(input("Give variable for power: \n"))
        if var:
            output = self.__calc_func.pow(var)
            self.__history.append(["Power", var, output])
            print(output)

    def exec_add(self):
        var = [int(x) for x in input("Give addition: \n").split()]
        if var:
            output = self.__calc_func.add(var)
            self.__history.append(["Multiply", var, output])
            print(output)

    def exec_multiply(self):
        var = [int(x) for x in input("Give multiplication: \n").split()]
        if var:
            output = self.__calc_func.multiply(var)
            self.__history.append(["Multiply", var, output])
            print(output)
