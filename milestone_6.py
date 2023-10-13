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
        self.letters_remaining = word_to_be_guessed
        


    def check_guess(self, guessed_letter):
        if guessed_letter in self.letters_remaining:
            print(f"Good guess! {guessed_letter} is in this word")

            for letter in word_to_be_guessed:
                letter_index = word_to_be_guessed.index(letter)

                if guessed_letter == letter and guessed_letter != self.word_guessed[letter_index]:
                    self.word_guessed[letter_index] = guessed_letter
                else:
                    continue
            self.num_letters -= 1
            self.letters_remaining = self.letters_remaining.replace(guessed_letter,"",1)
        elif guessed_letter in self.list_of_guesses:
            print("You have already guessed")
        else:
            print(f"Unlucky! {guessed_letter} is not in the word") 
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives remaining")


    def ask_for_letter(self):
        print(self.word_guessed)
        users_guess  = str(input("Guess a letter: ").lower())
        if not len(users_guess) == 1 or not users_guess.isalpha():
            print("Invalid input. Please enter a single alphabetical character.")
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
            print(game.letters_remaining)
        elif game.num_letters == 0:
            print("You Win!!!")        
            Game_On = False

play_game(guess_word_list)
