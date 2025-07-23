person = "Long"
coins = 3

massage01 = "\n"+person+" has " + str(coins) + " in the game." 
print(massage01)

massage02 = "\n%s has %s in the game" % (person, coins)
print(massage02)

massage03 = f"\n{person} has {coins} in the game" # can use all the method like when pushing in the print with no ""
print(massage03)

massage04 = "\n{} has {} in the game".format(person, coins)
print(massage04)

massage05 = "\n{1} has {0} in the game".format(person, coins) #flip the order
print(massage05)

massage06 = "\n{meow} has {hah} in the game".format(meow = person, hah = coins)
print(massage06)

player = {
    "name" : "long",
    "coins" : 3
}

massage07 = "\n{name} has {coins} in the game".format(**player) #this is how to pass a dict in using **<name>
print(massage07)

num = 10 
print(f"\n2.25 times {num} is {2.25 * num:.3f}") # print 2 number after the decimal number fixed and it must use in string formating or fstring

print(f"percent {num/3:5%}") #add the "%" at the end with 5 numbers after "."
#can come to w3school to see more formating 
