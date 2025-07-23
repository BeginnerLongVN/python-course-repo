# String data type
last_name = "long"
first_name = "doan"

# print(type(last_name))
# print(type(first_name) == str)
# print (isinstance(first_name, str))

# # constructor function 
# pizza = str("peperoni")
# print(type(pizza))
# print(isinstance(pizza, str))

# concatenation 
fullname = first_name + " " + last_name
print(fullname)

#casting a number to string 
decade = str(2025)
print (type(decade))

statement = "I like computer " + decade 
print(statement)

#multiline 
multiline = """
                    hello bro                                                
        how are you     
    are you ok

"""
print(multiline)

#escaping special characters
sentence = 'I\'m the first one come here\t and my first is so cool\n\n how old are you\\fine\\not good'
print(sentence)

#String method
print(first_name.lower())
print(first_name.upper())
print(fullname.title()) 
print(fullname)

print(multiline.replace("ok", "good"))
print(multiline)

print (len(multiline))
print(multiline.strip())
print(len(multiline))

#build a drinking menu
title = str("menu")
title = title.upper()
title = title.center(30,"=")
print(title)
drink01 = "Coffee".ljust(16,".") + "$30".rjust(14)
drink02 = "Water".ljust(17,".") + "$20".rjust(13)
drink03 = "Cola".ljust(18, ".") + "$21".rjust(12)
print(drink01 + "\n" + drink02 + "\n" + drink03)

#Some methods return bool data
print(first_name.startswith("d"))
print(last_name.endswith("g"))

#boolean data type
x = bool(True) 
print(type(x))

# Numeric data type
#int type 
#float type 
#complex type 
comp_type = 5+3j 
print(comp_type.real)
print(comp_type.imag)

#builtin functions for number 
gpa = 2.871
print(abs(gpa))
print(round(gpa, 1))
print(round(gpa,2))

import math
print(math.pi)
print(math.sqrt(64))
print(math.floor(gpa))
print(math.ceil(gpa))

#casting string to int
number = "1000000"
number = int(number)
print(type(number))
