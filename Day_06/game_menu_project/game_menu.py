import sys 
from game_rolling_dices import play_rolling_dices
from ROCK_PAPER_SCISSORS import play_rock_paper_scissors
from GUESSING_NUMBER import play_guess_num

def show_game_menu(player_name): 
    
    print("GAME MENU".center(20,'='))
    game_choice = input("1. ROLLING DICE 🎲\n2. ROCK PAPER SCISSORS 🪨 📄 ✂️\n3. NUMBER GUESSING 🔢\nOr 'Q' to quit\nYour choice: ")

    if (game_choice.lower() not in "123q") or (len(game_choice)>1): 
        print("Invalid choice")
        game_choice = input("1. ROLLING DICE 🎲\n2. ROCK PAPER SCISSORS 🪨 📄 ✂️\n3. NUMBER GUESSING 🔢\nOr 'Q' to quit\nYour choice: ")
        
    if game_choice == '1': 
        game01 = play_rolling_dices(player_name)
        game01()
        show_game_menu(player_name)
    elif game_choice == '2': 
        game02 = play_rock_paper_scissors(player_name)
        game02()
        show_game_menu(player_name)
    elif game_choice == '3': 
        play_guess_num(player_name)
        show_game_menu(player_name)
    else: 
        print(f"{player_name}, Thankyou for having me! ")
        sys.exit()

if __name__ == "__main__": 
    player_name = input("Type in your name: \n") 
    show_game_menu(player_name)
        

    