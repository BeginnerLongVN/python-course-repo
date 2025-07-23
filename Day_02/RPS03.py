import sys
import random
from enum import Enum 

def play_games() : 
    player_input = input("GAME MENU\n1 for Rock\n2 for paper\n3 for Scissors\n\n")
    player_choice = int(player_input)
    if player_choice<1 | player_choice>3: 
        sys.exit("You must choose number 1,2 or 3!")
        
    computer_choice = random.randint(1,3)
    # Display output of two user
    print("You chose " + str(RPS(player_choice)).replace("RPS.", "")) 
    print("Computer chose " + str(RPS(computer_choice)).replace("RPS.", "")) 

    # Display game final
    ok = True

    if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        print("🎉 You win! 🎉")
    elif player_choice == computer_choice:
        print("A tied game!")
    else:
        ok = False
        print("computer dominate you!")

    play_again_input = input("Do you want to play again? (Y/N) ") 
    if play_again_input.lower() == "n": 
        playagain = False
        print("welcome to play again")
        print("It's a good game")
    else: 
        print("\n")
        play_games()

class RPS(Enum): 
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
play_games()

sys.exit("bye bye")