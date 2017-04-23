from random import randint


class MadLibs(object):
    __sentence = ["{}! he said {} as he jumped into his convertible\n"
                  "{}"
                  "{} and drove off with his {} wife. "
                  "{}",
                  "{}! she said as she jumped into the {} \n"
                  "{}"
                  "{} and drove off with his {}. "
                  "{}"
                  ]

    def run(self):
        sentence = self.start_up()
        while True:
            var = [str(x) for x in input("Fill in the words\n").split()]
            if len(var) == 4:
                print(self.__sentence[sentence].format(var[0], var[1], '', var[2], var[3], ''))
                if input("Good job!\nPlay again?: y/n:\n") == 'y':
                    sentence = self.start_up()
                    continue
            else:
                print("Wrong number of lines inputted\nTry again")
                continue
            break

    def start_up(self):
        sentence = randint(0, len(self.__sentence) - 1)
        print(self.__sentence[sentence].format("_____________", "________",
                                               "exclamation            adverb\n",
                                               "______", "______",
                                               "\nnoun                          adjective"))
        return sentence
