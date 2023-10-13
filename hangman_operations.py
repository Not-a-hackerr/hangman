import random as rd
from os import system


guess_word_list = ["Pineapple"]
word_to_be_guessed = rd.choice(guess_word_list).lower()

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = int(num_lives)
        self.word_guessed = ["_" for num_of_letters_in_word in word_to_be_guessed]
        self.list_of_guesses = []
        self.num_letters = len(word_to_be_guessed)
        self.letters_remaining = word_to_be_guessed


    def check_guess(self, guessed_letter):
        if guessed_letter in self.letters_remaining:
            # system("clear")
            print(f"Good guess! {guessed_letter} is in this word")

            for letter in word_to_be_guessed:
                letter_index = word_to_be_guessed.index(letter)

                if guessed_letter == letter and self.word_guessed[letter_index] == "_": 
                    self.word_guessed[letter_index] = guessed_letter
                    self.num_letters -= 1
                    self.letters_remaining = self.letters_remaining.replace(guessed_letter,"",1)
                    
                else:
                    continue
        elif guessed_letter in self.list_of_guesses:
            # system("clear")
            print("You have already guessed")
        else:
            # system("clear")
            print(f"Unlucky! {guessed_letter} is not in the word") 
            self.num_lives -= 1


    def ask_for_letter(self):
        # system("clear")
        print(f"Remaining lives: {self.num_lives}")
        print(self.word_guessed)
        print(f"These are the letters you have tried {self.list_of_guesses}")
        print(self.letters_remaining)
        users_guess  = str(input("Guess a letter: ").lower())
        if not len(users_guess) == 1 or not users_guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
        else:
            self.check_guess(users_guess)
            self.list_of_guesses.append(users_guess)