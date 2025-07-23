from random import choice

def play_rock_paper_scissors(player_name="Long"): 
    rps = {
        1: "ROCK 🪨🪨🪨",
        2: "PAPER 📃📃📃",
        3: "SCISSORS ✂️✂️✂️"
    }
        
    game_count = 0
    player_wins = 0 
    computer_wins = 0 
    
    def play(): 
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins
        game_count += 1
        player_choice = int(input(f"Welcome to game number {game_count}, {player_name}\nGame menu".center(30,'=')+"\n"+"1. Rock".ljust(30,'.')+"\n"+"2. Paper".ljust(30,'.')+'\n'+"3. Scissors".ljust(30,'.')+"\n"+"your choice: "))
        print('\n')
        while str(player_choice) not in "123": 
            print("Invalid choice")
            player_choice = int(input("Game menu".center(30,'=')+"\n"+"1. Rock".ljust(30,'.')+"\n"+"2. Paper".ljust(30,'.')+'\n'+"3. Scissors".ljust(30,'.')+"\n"))
        
        computer_choice = int(choice("123"))
        if (player_choice==1 and computer_choice==3) or (player_choice==2 and computer_choice==1) or (player_choice==3 and computer_choice==2): 
            game_result = "🎉Congratulation, you win🎉"
            player_wins += 1
        elif computer_choice == player_choice: 
            game_result = "😆It's a tie game😆"
        else: 
            game_result = "😎Computer dominates you😎"
            computer_wins += 1
            
        print(f"You chose {rps[player_choice]}")
        print(f"Computer chose {rps[computer_choice]}")
        print(game_result)
        print(f"{player_name}'s wins = {player_wins}")
        print(f"Computer wins {computer_wins}")
        print(f"Your win rate is : {player_wins/game_count:.2%}\n")
        
        play_again = input("Do you want to play again?(Y or N): ")
        while (play_again.lower() not in "yn") or (len(play_again)!=1): 
            print("Invalid choice") 
            play_again = input("Do you want to play again?(Y or N): ")
            
        if play_again.lower() == 'n': 
            print(f"Bye bye {player_name}")
            return 
        
        play()
    
    return play
        

def main(): 
    play_game = play_rock_paper_scissors()
    play_game()

if __name__ == "__main__": 
    main()