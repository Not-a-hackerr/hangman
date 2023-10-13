import random as rd

guess_word_list = ["Pineapple", "Mango", "Plum", "Banana", "Orange"]
word_to_be_guessed = rd.choice(guess_word_list).lower()
print(word_to_be_guessed)

while True:
    users_guess  = input("Guess a letter: ").lower()
    if len(users_guess) == 1 and users_guess.isalpha(): 
        if users_guess in word_to_be_guessed:
            print(f"Good guess! {users_guess} is in this word")
        else:
            print(f"Unlucky! {users_guess} is not in the word") 
    else:
        print("Invalid input. Please, enter a single alphabetical character.")

