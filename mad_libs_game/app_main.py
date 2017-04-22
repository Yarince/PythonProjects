class MadLibs(object):
    __sentence = "{}! he said {} as he jumped into his convertible\n" \
                 "{}" \
                 "{} and drove off with his {} wife. " \
                 "{}"

    def run(self):

        print(self.__sentence.format("_____________", "________",
                                     "exclamation            adverb\n",
                                     "______", "______",
                                     "\nnoun                          adjective"))
        while True:
            var = [str(x) for x in input("Fill in the words\n").split()]
            if len(var) == 4:
                print(self.__sentence.format(var[0], var[1], '', var[2], var[3], ''))
            else:
                print("Wrong number of lines inputted\nTry again")
            break


def main():
    MadLibs().run()


if __name__ == '__main__':
    main()
