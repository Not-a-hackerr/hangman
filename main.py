import hangman_operations as hm
from os import system

def play_game(word_list):
    game = hm.Hangman(word_list)
    Game_On = True
    while Game_On:
        if game.num_lives == 0:
            print("You have lost!")
            Game_On = False
        elif game.num_letters > 0:
            game.ask_for_letter()
        elif game.num_letters == 0:
            print("You Win!!!")
            print(game.num_letters)        
            Game_On = False


Play_Again = True
while Play_Again:
    play_game(hm.guess_word_list)
    play_again = input("Do you want to play again? (Type y for yes and n for no):")
    if play_again == "n":
        print("Good byeeee!")
        Play_Again = False