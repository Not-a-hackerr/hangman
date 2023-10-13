import random as rd

guess_word_list = ["Pineapple", "Mango", "Plum", "Banana", "Orange"]
word_to_be_guessed = rd.choice(guess_word_list).lower()
print(word_to_be_guessed)


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

   


while True:
    letter = ask_for_letter()
    check_guess(letter)
