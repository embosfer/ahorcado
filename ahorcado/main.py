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

    def __str__(self):
        return ' '.join(self.current_word) + '\n\n' + ','.join(self.letters_used) + '\n'

    def play(self):
        while not self.hung() and not self.freed():
            print(self)
            letter = input('Which letter? ')
            self.check_ifexists(letter)

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
        return self.strikes == 9

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
