import random as rd

guess_word_list = ["Pineapple", "Mango", "Plum", "Banana", "Orange"]
word_to_be_guessed = rd.choice(guess_word_list).lower()
print(word_to_be_guessed)


def ask_for_letter():
    while True:
        users_guess  = input("Guess a letter: ").lower()
        if len(users_guess) == 1 and users_guess.isalpha():
            check_guess(users_guess)
        else:
            print("Invalid input. Please enter a single alphabetical character.")


def check_guess(guessed_letter):
    if guessed_letter in word_to_be_guessed:
        print(f"Good guess! {guessed_letter} is in this word")
    else:
        print(f"Unlucky! {guessed_letter} is not in the word") 
    

ask_for_letter()



# while True:
#     letter = ask_for_letter()
#     check_guess(letter)



