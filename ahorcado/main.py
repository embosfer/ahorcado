"""
Python implementation of Ahorcado (Hangman)
                  ____
                 |    |
                 |    O
                 |   -|-
                 |   /\
                _|_

_ _ _ _ _

A,C,H,N

"""


class Ahorcado:

    def __init__(self, word_to_guess):
        if word_to_guess.isnumeric() or word_to_guess == '':
            raise TypeError('Input must be a word!')

        self.word = word_to_guess.upper()
        self.current_word = ['_' for _ in word_to_guess]
        self.letters_used = []
        self.strikes = 0
        self.letters_left = len(word_to_guess)
        self.hangman = ['' for _ in range(6)]

    def __str__(self):
        return ''.join(reversed(self.hangman)) + '\n\n' + ' '.join(self.current_word) + '\n\n' + ','.join(self.letters_used) + '\n'

    def refresh_hangman(self):
        if self.strikes == 1:
            self.hangman[0] = '\t\t\t_|_\n'
        elif self.strikes == 2:
            self.hangman[1] = '\t\t\t |\n'
        elif self.strikes == 3:
            self.hangman[2] = '\t\t\t |\n'
        elif self.strikes == 4:
            self.hangman[3] = '\t\t\t |\n'
        elif self.strikes == 5:
            self.hangman[4] = '\t\t\t |\n'
        elif self.strikes == 6:
            self.hangman[5] = '\t\t\t  ____\n'
        elif self.strikes == 7:
            self.hangman[4] = self.hangman[4][:-1] + '    |\n'
        elif self.strikes == 8:
            self.hangman[3] = self.hangman[3][:-1] + '    O\n'
        elif self.strikes == 9:
            self.hangman[2] = self.hangman[2][:-1] + '   -|- \n'
        elif self.strikes == 10:
            self.hangman[1] = self.hangman[1][:-1] + '   / \ \n'

    def play(self):
        while not self.hung() and not self.freed():
            print(self)
            letter = input('Which letter? \n\n')
            self.check_ifexists(letter)
            self.refresh_hangman()

        print(self)
        self.print_finalresult()

    def print_finalresult(self):
        print('')
        if self.hung():
            print('GAME OVER')
            print('The word was "{}".'.format(self.word))
        else:
            print('Well done!')

    def hung(self):
        return self.strikes == 10

    def freed(self):
        return self.letters_left == 0

    def check_ifexists(self, letter):
        letter = letter.upper()
        if self.already_used(letter):
            return

        self.letters_used.append(letter)
        was_miss = self.apply_againstword(letter)

        if was_miss:
            self.strikes += 1

        return not was_miss

    def apply_againstword(self, letter):
        was_miss = True
        for index, char in enumerate(self.word):
            if char == letter:
                self.current_word[index] = letter
                self.letters_left -= 1
                was_miss = False
        return was_miss

    def already_used(self, letter):
        if letter in self.letters_used:
            print('The letter {} has been used already! Choose another one...'.format(letter))
            return True
        return False


def main():
    word = input('Give me a word to guess: ')
    ahorcado = Ahorcado(word)
    ahorcado.play()


if __name__ == '__main__':
    main()
