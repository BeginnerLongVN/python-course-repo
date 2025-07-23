import sys
import random
from enum import Enum 

def play_ROCK_PAPER_SCISSORS(name="long"):
    game_count = 0
    player_wins = 0
    computer_wins = 0
    def play_games() : 
        
        class RPS(Enum): 
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        
        nonlocal game_count 
        game_count += 1
        player_input = input(f"WELCOME {name} to game number {game_count} \nGAME MENU\n1 for Rock\n2 for paper\n3 for Scissors\n\n")
        
        while player_input not in "123": 
            player_input = input(f"{name}, come on just choose 1, 2, or 3")
        
        player_choice = int(player_input)
        if player_choice<1 | player_choice>3: 
            sys.exit("You must choose number 1,2 or 3!")
            
        computer_choice = random.randint(1,3)
        # Display output of two user
        print("You chose " + str(RPS(player_choice)).replace("RPS.", "")) 
        print("Computer chose " + str(RPS(computer_choice)).replace("RPS.", "")) 

        # Display game final
        def game_result(player_choice, computer_choice) : 
            nonlocal player_wins
            nonlocal computer_wins
            if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
                player_wins += 1
                return "🎉 You win! 🎉 "
            elif player_choice == computer_choice:
                return "A tied game! "
            else:
                computer_wins += 1
                return "🤪computer dominate you!🤪"

        print(game_result(player_choice, computer_choice), end="\n\n") 
        print(f"You got {player_wins}")
        print(f"Computer got {computer_wins}")
        
        
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
                
    return play_games()


if __name__ == "__main__": 
    play_ROCK_PAPER_SCISSORS()

