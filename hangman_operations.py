import random as rd
from os import system


# guess_word_list = [
#     "pineapple", "apple", "aango", 
#     "plum", "tangerine", "orange",
#     "grapes", "watermelon", "banana"
#     ]
guess_word_list = ["pinapple"]

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_to_be_guessed = rd.choice(guess_word_list)
        self.word_list = word_list
        self.num_lives = num_lives
        self.word_guessed = ["_" for letter in self.word_to_be_guessed]
        self.list_of_guesses = set()
        self.num_letters = len(self.word_to_be_guessed)


    def check_guess(self, guessed_letter):
        """
        Checks if the letter typed has either been typed already,
           not in the word or is in the word
           If the letter is in the word it will fill in all the letter in the word
        """

        if guessed_letter in self.list_of_guesses:
            # Clears the terminal window which enhaces the gaming experiece better
            system("clear")
            print("You have already guessed")

        elif guessed_letter in self.word_to_be_guessed:
            system("clear")
            print(f"Good guess! {guessed_letter} is in this word")

            for LetterPlace in (idx for idx,l in enumerate(self.word_to_be_guessed) if l==guessed_letter):
                self.word_guessed[LetterPlace] = guessed_letter
            """
             This nested for loop goes through the word to be guessed once the letter guessed is
             equal to a letter in the word it saves the index of that letter in the word and 
             tells uses the same index to replace an _ with the correct letter
             """
            self.num_letters -= 1
       
        else:
            system("clear")
            print(f"Unlucky! {guessed_letter} is not in the word") 
            self.num_lives -= 1


    def ask_for_letter(self):
        # Prints all relevant information that a player may need to make another guess
        print(f"Remaining lives: {self.num_lives}")
        print(f"These are the letters you have tried {self.list_of_guesses}")
        print(self.word_guessed)
        users_guess  = input("Guess a letter: ").lower()

        if not len(users_guess) == 1 or not users_guess.isalpha():
            system("clear")
            print("Invalid input. Please enter a single alphabetical character.")

        else:
            self.check_guess(users_guess)
            self.list_of_guesses.add(users_guess)

  
def play_game(word_list):
    game = Hangman(word_list)  
    Game_On = True
    while Game_On:
        if game.num_lives == 0:
            print(f"You lost! \nThe word was {game.word_to_be_guessed}")
            Game_On = False
        elif "_" in game.word_guessed:
            game.ask_for_letter()
        elif "_" not in game.word_guessed:
            print(game.word_guessed)
            print(f"You Win!!!")
            Game_On = False             


if __name__ == "__main__":
    Play_Again = True
    while Play_Again:
        system("clear")
        play_game(guess_word_list)
        play_again = input("Do you want to play again? (Type y for yes and n for no):")
        if play_again == "n":
            system("clear")
            print("Good byeeee!")
            Play_Again = False
