"""
Little "Guess the number" game from "Invent your own computer games with python" by Al Sweigart
(Given rules but my own code)
"""

import random


# --------- STATIC FUNCTIONS ----------
def greetings():
    print("Hello there. What's your name?")
    user_name = input()
    print("Hello ", user_name, ". I am thinking of a number between 1 and 20. Can you guess it?")
    return user_name


def play_again():
    print("Wanna try again? (y/n)")
    again = input()
    if again == "y":
        print("Ok then, take a guess!")
        return True
    else:
        print("Ok, bye!")
        return False


# --------- CLASS ----------
class GuessTheNumber:

    def __init__(self):
        self.user_name = greetings()
        self.guessing()

    def guessing(self):
        number = random.randint(1, 20)
        guessed = False
        while not guessed:
            guessed = self.check(number)
        if play_again():
            self.guessing()

    def check(self, number):
        guess = input()
        if int(guess) == int(number):
            print("Good job, ", self.user_name, "!")
            return True
        elif int(guess) < int(number):
            print("Too low, guess again.")
            return False
        elif int(guess) > int(number):
            print("Too high, guess again.")
            return False
        else:
            print("number: ", number, " guess: ", guess)


def main():
    game = GuessTheNumber()


if __name__ == '__main__':
    main()
