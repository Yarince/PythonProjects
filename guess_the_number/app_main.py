from random import randint


class GuessTheNumber(object):
    __max = 0
    __min = 0

    def __init__(self, min_value, max_value):
        self.__min = min_value
        self.__max = max_value

    def run(self):
        while True:
            answer = randint(self.__min, self.__max)
            reply = 0
            try:
                reply = int(input("Guess the number: \n"))
                if not (self.__min <= reply <= self.__max):
                    raise ValueError()
            except ValueError:
                print("Invalid Option, you needed to choose a number between %d and" % self.__min, self.__max)
            if reply == answer:
                print("     Gratz!")
                if input("Continue? \n") == 'y':
                    continue
                else:
                    break
            else:
                print("     :( \n Number was %d" % answer)


def main():
    GuessTheNumber(0, 2).run()


if __name__ == '__main__':
    main()
