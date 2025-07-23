from guess_num import play_guess_num
from RPS07 import play_ROCK_PAPER_SCISSORS

def game_menu() :
    name = input("Enter your name: " )
    game_choice = "0"
    
    while game_choice != "3": 
        game_choice = input(f"{name}, which game you want to play?\n1. ROCK PAPER SCISSORS\n2. GUESSING NUMBER\nOr 3 to QUIT\n")

        if game_choice == "1": 
            play_ROCK_PAPER_SCISSORS(name)
        elif game_choice == "2" : 
            play_guess_num(name)
    else : 
        print(f"{name}, See yah")
        return 

if __name__ == "__main__": 
    game_menu()

