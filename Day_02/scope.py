menu = 0

def show_menu():
    print(menu) #access to globle variable 
    
def change_menu() : 
    global menu #change the global variable 
    menu += 1
    print(menu)
    
def parent():
    blue = 1
    def show_color():
        nonlocal blue
        print(blue)
        print(menu)
         #change parent's variable 
        blue = 2
        
    show_color()

#keynote: chilren can access every outer scope 
#use globle and nonlocal to change the variable 
#when you want to change and use the base global variable at the same time use must define global or nonlocal at the very first.
show_menu()
change_menu()
parent()