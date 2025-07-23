from random import randint

def play_guess_num(player_name="long"): 
    print(f"Welcome to Guess number game {player_name}")
    final_answer = randint(1,100)
    guess_count = 0
    player_choice = -1
    while player_choice != final_answer: 
        player_choice = int(input("Guess the number between 1 and 100: "))
        if player_choice>final_answer: 
            print("Too high")
        elif player_choice<final_answer: 
            print("Too low")
        guess_count += 1
    else: 
        print(f"🎉Congratulation you guessed the number after {guess_count} times")
        
    return 
    

def main(): 
    play_guess_num("long")

if __name__ == "__main__": 
    main()

