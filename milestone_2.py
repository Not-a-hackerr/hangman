import random as rd

word_list = ["Pineapple", "Mango", "Plum", "Banana", "Orange"]
print(rd.choice(word_list))

guess = input("Guess a letter: ")

if len(guess) == 1 and guess.isalpha(): 
    print("Good guess!!")
else:
    print("This is not a valid input")
    
    