import sys 
import random

def play_guess_num(player_name="long") : 
    game_count = 0
    player_wins = 0 
    def play_game() :
        nonlocal game_count 
        nonlocal player_wins
        player_input = input(f"{player_name}, guess what number I'm thinking of ..., 1, 2, or 3\n")
        while player_input not in "123": 
            player_input = input(f"Common {player_name} only 1, 2, or 3\n")
        
        game_count += 1
        
        computer_choice = random.choice("123") 
        
        if (computer_choice == player_input): 
            print(f"{player_name}, you win 🎉🎉🎉")
            player_wins += 1
        else : 
            print(f"It's a pitty {player_name}, please try again 🥲🥲🥲")

        print(f"Game you play: {game_count}")
        print(f"{player_name} win {player_wins}")
        print(f"{player_name}'s winning percentage = {player_wins/game_count:.2%}")


        play_again = input(f"{player_name}, do you want to play again?\nY for play Or\nQ for quit\n")
        while play_again.lower() not in "yq": 
            play_again = input(f"{player_name}, please be serious!!! Y or Q")
        
        if play_again.lower() == "y": 
            play_game()
        else : 
            print(f"Bye bye {player_name}, see you again\n")
            return 
    
    return play_game

if __name__ == "__main__": 
    play = play_guess_num()
    play()

        
        
        
