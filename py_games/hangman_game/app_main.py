class Hangman(object):
    __lives = 10
    __guesses = 0
    __answer = ""

    def __init__(self, lives):
        self.__lives = lives
        self.__answer, self.__word = self.start_up()

    def run(self):
        while True:
            print("Lives = ", self.__lives)
            if self.__lives <= 0:
                print("AF!")
                break
            print("Word is = ", self.__word)
            if self.__word == self.__answer:
                print("Congratulations!\n"
                      "You had %d guesses" % self.__guesses)
                if input("Want to play again? y/n:\n") == 'y':
                    self.__answer, self.__word = self.start_up()
                    continue
                else:
                    break

            guess = input("Guess:\n")
            self.__guesses += 1
            if len(guess) == 1:
                self.__word = self.check_guess(self.__answer, guess, self.__word)
            else:
                if guess == self.__answer:
                    print("Congratulations!\n"
                          "You had %d guesses" % self.__guesses)
                    if input("Want to play again? y/n:\n") == 'y':
                        self.__answer, self.__word = self.start_up()
                        continue
                    else:
                        break
                else:
                    print("Wrong guess. -3 lives!")
                    self.__lives -= 3

    def check_guess(self, answer, guess, word):
        if guess in answer:
            i = 0
            answer_list = list(answer)
            while i < len(answer_list):
                if answer_list[i] == guess:
                    word = self.change_letter(word, guess, i)
                i += 1
        else:
            self.__lives -= 1
        return word

    def start_up(self):
        self.__lives = 10
        self.__guesses = 0
        answer = input("What is the word to be guessed?\n")
        word = '_' * answer.__len__()
        return answer, word

    @staticmethod
    def change_letter(string, letter, index):
        string_list = list(string)
        string_list[index] = letter
        return "".join(string_list)


class Main:
    Hangman(10).run()


if __name__ == '__main__':
    Main()
