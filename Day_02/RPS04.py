import sys
import random
from enum import Enum 

game_count = 0

def play_games() : 
    global game_count 
    game_count += 1
    player_input = input(f"WELCOME TO game number {game_count} \nGAME MENU\n1 for Rock\n2 for paper\n3 for Scissors\n\n")
    player_choice = int(player_input)
    if player_choice<1 | player_choice>3: 
        sys.exit("You must choose number 1,2 or 3!")
        
    computer_choice = random.randint(1,3)
    # Display output of two user
    print("You chose " + str(RPS(player_choice)).replace("RPS.", "")) 
    print("Computer chose " + str(RPS(computer_choice)).replace("RPS.", "")) 

    # Display game final
    ok = True
    def game_result(player_choice, computer_choice) : 
        if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
            return "🎉 You win! 🎉 "
        elif player_choice == computer_choice:
            return "A tied game! "
        else:
            ok = False
            return "🤪computer dominate you!🤪"

    print(game_result(player_choice, computer_choice), end="\n\n") 
    
    
    while True: 
        play_again_input = input("Do you want to play again? (Y/N) ") 
        if play_again_input.lower() == "n": 
            playagain = False
            print("welcome to play again")
            print("It's a good game")
            break
        elif play_again_input.lower() == 'y':
            print("\n")
            play_games()
            break
        else: 
            print("please be serious!")
            

class RPS(Enum): 
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
play_games()

sys.exit("bye bye")