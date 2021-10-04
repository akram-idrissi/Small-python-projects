import random


class Bagel:
    def __init__(self, num_digit=3, max_guesses=10):
        self.num_digit = num_digit
        self.max_guesses = max_guesses
        self.secret_number = self.get_secret_number()

    def get_secret_number(self):
        secret_number = ""
        digits = list(range(0, 10))

        for i in range(self.num_digit):
            random_digits = random.choice(digits)
            secret_number += str(random_digits)

        return secret_number

    def get_clues(self, guess, secret_number):
        clues = []

        if guess == secret_number:
            return "You got it"

        for i in range(self.num_digit):
            if guess[i] == secret_number[i]:
                clues.append("Fermi")
            elif guess[i] in secret_number:
                clues.append("Pico")

        if len(clues) == 0:
            return "Bagles"
        else:
            return " ".join(clues)

    def run(self):
        print('''Bagels, a deductive logic game.
        I am thinking of a {}-digit number with no repeated digits.
        Try to guess what it is. Here are some clues:
        When I say: That means:
        Pico One digit is correct but in the wrong position.
        Fermi One digit is correct and in the right position.
        Bagels No digit is correct.
        For example, if the secret number was 248 and your guess was 843, the
        clues would be Fermi Pico.'''.format(self.num_digit))

        while True:
            num_guesses = 1
            secret_number = self.get_secret_number()
            print('I have thought up a number.')
            print(' You have {} guesses to get it.'.format(self.max_guesses))

            while num_guesses <= self.max_guesses:
                guess = ""

                while len(guess) != self.num_digit and not guess.isdecimal():
                    print('Guess #{}: '.format(num_guesses))
                    guess = input("> ")

                clues = self.get_clues(guess, secret_number)
                print(clues)
                num_guesses += 1

                if guess == secret_number:
                    break
                if num_guesses > self.max_guesses:
                    print('You ran out of guesses.')
                    print('The answer was {}.'.format(secret_number))

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for playing!')


if __name__ == "__main__":
    # num_digit = 5
    # max_guesses = 15
    app = Bagel()
    app.run()
