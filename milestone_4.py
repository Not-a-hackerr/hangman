import random as rd

guess_word_list = ["Pineapple", "Mango", "Plum", "Banana", "Orange"]
word_to_be_guessed = rd.choice(guess_word_list).lower()
print(word_to_be_guessed)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = int(num_lives)
        word = word_to_be_guessed
        self.word_guessed = ["_" for num_of_letters_in_word in word]
        self.list_of_guess = []
        # print(self.word_guessed)

    def ask_for_letter():
        users_guess  = input("Guess a letter: ").lower()
        return users_guess 
    
    def check_guess(guessed_letter):
        guessed_letter = str(guessed_letter)
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            if guessed_letter in word_to_be_guessed:
                print(f"Good guess! {guessed_letter} is in this word")
            else:
                print(f"Unlucky! {guessed_letter} is not in the word") 
        else:
            print("Invalid input. Please, enter a single alphabetical character.")


game = Hangman(guess_word_list)

