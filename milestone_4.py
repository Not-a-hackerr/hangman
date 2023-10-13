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
        self.list_of_guesses = []
        print(self.word_guessed)

    def check_guess(self, guessed_letter):
        if guessed_letter in word_to_be_guessed:
            print(f"Good guess! {guessed_letter} is in this word")
        else:
            print(f"Unlucky! {guessed_letter} is not in the word") 


    def ask_for_letter(self):
        while True:
            users_guess  = str(input("Guess a letter: ").lower())
            if not len(users_guess) == 1 or not users_guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
            elif users_guess in self.list_of_guesses:
                print("You have already guessed")
            else:
                self.check_guess(users_guess)
                self.list_of_guesses.append(users_guess)
        

  

    


game = Hangman(guess_word_list)

game.ask_for_letter()

