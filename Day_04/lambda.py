squared = lambda num: num * num #num is parameter

print(squared(2))

sum = lambda a, b: a + b #a, b are parameters

print(sum(2,3))

####################################

def buildfunc(x): 
    return lambda num: num + x

addten = buildfunc(10) # using x for parameter 
addtwenty = buildfunc(20)

print(addten(7)) # using num for parameter 
print(addtwenty(7)) 

#######################################

def square_num(num): 
    return num * num

nums = [2, 3, 4, 5, 12, 13]
squared_nums01 = map(lambda num: num * num, nums) 
# map is used to redone a list to a new list using a lambda function to redone the elements in the list
print(list(squared_nums01))

########################################

odd_nums = filter(lambda num: num % 2 != 0, nums)
#using filter to filt nums that has the lambda condition and create a new list
print(list(odd_nums))
# to print map, filter list we must add list() in front of them. If not it will print the preferences

#########################################

