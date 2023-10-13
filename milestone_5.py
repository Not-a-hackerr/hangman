import random as rd

guess_word_list = ["Mango", "Plum", "Orange"]
word_to_be_guessed = rd.choice(guess_word_list).lower()
print(word_to_be_guessed)


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = int(num_lives)
        self.word_guessed = ["_" for num_of_letters_in_word in word_to_be_guessed]
        self.list_of_guesses = []
        self.num_letters = len(word_to_be_guessed)
        


    def check_guess(self, guessed_letter):
        if guessed_letter in word_to_be_guessed:
            print(f"Good guess! {guessed_letter} is in this word")
            for letter in word_to_be_guessed:
                if guessed_letter == letter:
                    letter_index = word_to_be_guessed.index(letter)
                    self.word_guessed[letter_index] = guessed_letter
            self.num_letters -= 1                        
        else:
            print(f"Unlucky! {guessed_letter} is not in the word") 
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining")


    def ask_for_letter(self):
        print(self.word_guessed)
        users_guess  = str(input("Guess a letter: ").lower())
        if not len(users_guess) == 1 or not users_guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
        elif users_guess in self.list_of_guesses:
            print("You have already guessed")
        else:
            self.check_guess(users_guess)
            self.list_of_guesses.append(users_guess)
    

def play_game(word_list):
    game = Hangman(word_list)

    Game_On = True
    while Game_On:
        if game.num_lives == 0:
            print("You have lost!")
            Game_On = False
        elif game.num_letters > 0:
            game.ask_for_letter()
        elif game.num_letters == 0:
            print("You Win!!!")        
            Game_On = False

Play_Again = True
while Play_Again:
    play_game(guess_word_list)
    play_again = input("Do you want to play again? (Type y for yes and n for no):")
    if play_again == "n":
        print("Good byeeee!")
        Play_Again = False
