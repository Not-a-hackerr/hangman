import hangman_operations as hm
from os import system

def play_game(word_list):
    game = hm.Hangman(word_list)
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


Play_Again = True
while Play_Again:
    system("clear")
    play_game(hm.guess_word_list)
    play_again = input("Do you want to play again? (Type y for yes and n for no):")
    if play_again == "n":
        system("clear")
        print("Good byeeee!")
        Play_Again = False


