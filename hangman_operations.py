import random as rd
from os import system


guess_word_list = ["Pineapple"]


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_to_be_guessed = rd.choice(guess_word_list).lower()
        self.word_list = word_list
        self.num_lives = int(num_lives)
        self.word_guessed = ["_" for num_of_letters_in_word in self.word_to_be_guessed]
        self.list_of_guesses = set()
        self.num_letters = len(self.word_to_be_guessed)


    def check_guess(self, guessed_letter):
        if guessed_letter in self.word_to_be_guessed:
            system("clear")
            print(f"Good guess! {guessed_letter} is in this word")

            for LetterPlace in (idx for idx,l in enumerate(self.word_to_be_guessed) if l==guessed_letter):
                self.word_guessed[LetterPlace] = guessed_letter
            self.num_letters -= 1

        elif guessed_letter in self.list_of_guesses:
            system("clear")
            print("You have already guessed")
        else:
            system("clear")
            print(f"Unlucky! {guessed_letter} is not in the word") 
            self.num_lives -= 1


    def ask_for_letter(self):
        # system("clear")
        print(f"Remaining lives: {self.num_lives}")
        print(f"These are the letters you have tried {self.list_of_guesses}")
        print(self.word_guessed)
        users_guess  = str(input("Guess a letter: ").lower())
        if not len(users_guess) == 1 or not users_guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
        else:
            self.check_guess(users_guess)
            self.list_of_guesses.add(users_guess)