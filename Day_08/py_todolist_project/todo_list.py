import os 


def add(todo_lines_list, file):
    newtask = input("New task: ") 
    line = f"[{len(todo_lines_list)}] {newtask}"
    todo_lines_list.append(newtask)
    with open(file, "a") as pydo: 
        pydo.write("\n"+line)
    
    print("Task added!\n")

def list(file): 
    with open(file, "r") as pydo: 
        print(pydo.read() + "\n")

def remove(todo_lines_list, file): 
    task_remove_number = int(input("Enter task number you want to remove: "))
    del todo_lines_list[task_remove_number]
    with open(file, "w") as pydo: 
        for i in range(1,len(todo_lines_list)): 
            pydo.write("\n"+f"[{i}] {todo_lines_list[i]}")
            
    print("Task removed!")
    

def main(): 
    print("Welcome to Pydo! 🎉🎉🎉")
    namefile = "TODO_LIST.txt"
    
    if not os.path.exists(namefile): 
        todo_file = open(namefile, "x") 
        todo_file.close()
    
    with open(namefile, "r") as todo_file: 
        todo_lines = todo_file.read()
        
    print(todo_lines)
    
    todo_lines_list = todo_lines.split('\n') 
    todo_lines_list = [line[4:] for line in todo_lines_list]
    print("\n")
    
    option = "NONE"
    while option != "quit": 
        option = input("Enter command (add, list, remove, quit): ")
        while option.lower() not in ["add", "list", "remove", "quit"]: 
            print("Invalid input") 
            option = input("Enter command (add, list, remove, quit): ")
        
        if option == "add": 
            add(todo_lines_list, namefile)
        elif option == "list": 
            list(namefile)
        elif option == "remove": 
            remove(todo_lines_list, namefile)
    
    else: 
        print("Thank you for using our todo list! ")
    
if __name__ == "__main__": 
    main()