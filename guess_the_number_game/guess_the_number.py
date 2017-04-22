from random import randint


class GuessTheNumber(object):
    __max = 0
    __min = 0

    def __init__(self, min_value, max_value):
        self.__min = min_value
        self.__max = max_value

    def run(self):
        counter = 0
        answer = randint(self.__min, self.__max)
        while True:
            try:
                reply = int(input("Guess the number: \n"))
                if not (self.__min <= reply <= self.__max):
                    raise ValueError()
            except ValueError:
                print("Invalid Option, you needed to choose a number")
                continue
            if reply == answer:
                print("Congratulation your guess was correct! \n")
                print("You guessed %d time(s)" % counter)
                if input("Play again? y/n: ") == 'y':
                    answer = randint(self.__min, self.__max)
                    continue
                else:
                    break
            else:
                counter += 1
                self.calc_offset(answer, reply)

    @staticmethod
    def calc_offset(answer, reply):
        if reply > answer:
            print(":( \nNumber is to high")
        elif reply < answer:
            print(":( \nNumber is to low")
