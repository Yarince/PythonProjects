from pprint import pprint

from calculator.calculator_functions import CalculatorFunctions


class MyCalculator:
    """Calculator interface implementation"""

    def __init__(self):
        self.__calc_func = CalculatorFunctions()

    def run(self):
        while True:
            choice = str(input("What do you want to do?: m/a/pow/sqrt/history/X: m: \n") or 'm')
            if choice == 'm':
                var = [int(x) for x in input("Give multiplication: \n").split()]
                if var:
                    print(self.__calc_func.multiply(var))
            elif choice == 'a':
                var = [int(x) for x in input("Give addition: \n").split()]
                if var:
                    print(self.__calc_func.add(var))
            elif choice == 'pow':
                var = int(input("Give variable for power: \n"))
                if var:
                    print(self.__calc_func.pow(var))
            elif choice == 'sqrt':
                var = int(input("Give variable for square root: \n"))
                if var:
                    print(self.__calc_func.square_root(var))
            elif choice == 'X':
                break
            elif choice == 'history':
                pprint(self.__calc_func.get_history)
            else:
                continue
