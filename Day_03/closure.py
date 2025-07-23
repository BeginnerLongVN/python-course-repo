#closure is a function access the parent's scope 
# function after the parent function has return 

def parent_function(name, coins): 
    
    def play_games(): 
        nonlocal coins
        coins -= 1
        print(str(coins) + '\n') 
    
    return play_games

tommy = parent_function("tommy",5)

tommy()# tommy has 5 coins
tommy()# tommy has 4 coins
tommy()# tommy has 3 coins