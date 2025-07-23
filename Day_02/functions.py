def hello_world() :
    print("hello world")

hello_world()

def sum(num1 = 0, num2 = 0): 
    return num1+num2

print(sum(1))

def multiple_items(*args) :
    print(args)
    print(type(args))

multiple_items("meow", (5,6,7), [6,7], {4,3,5}, 'i')

def create_user(user_name, *roles, **atributes): 
    print(user_name)
    print(roles) #tuple
    print(atributes) #dict

create_user("long", "admin", code = "meow", respon = "playing") 