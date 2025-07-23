x = 2
try: 
    if type(x) is not str: 
        raise TypeError("Only string is allowed")
except Exception as error: 
    print(error)
finally: 
    print("I'm going to print with or without an error")