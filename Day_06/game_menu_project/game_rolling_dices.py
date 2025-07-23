from random import randint

def play_rolling_dices(name="Long"): 
    print("Welcome to Rolling dices game!".center(20,'='))
    game_count = 0 
    def play_game(): 
        nonlocal game_count
        game_count += 1
        # enter player choice 
        player_choice = input(f"\n{name}, game number {game_count}, Rolling the dice: (Y or N)\n")
        while (player_choice.lower() not in "yn") or (len(player_choice)>1): 
            print("Invalid choice")
            player_choice = input(f"\n{name}, game number {game_count}, Rolling the dice: (Y or N)\n")
            
        if player_choice.lower() == 'n': 
            print(f"Thank you for playing game 🎉🎉🎉")
            return 
        
        #generate dice 
        num1 = randint(1,6)
        num2 = randint(1,6)
        dice = (num1, num2)
        print(dice) 
        
        play_game()
    
    return play_game

def main(): 
    player_game = play_rolling_dices()
    player_game()
        
if __name__ == "__main__": 
    main()