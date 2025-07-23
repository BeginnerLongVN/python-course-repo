users = ['long', 'dave', 'meow']

print(users.index('long'))
print(users[0:-1])
print(users[0:])

print('long' in users)
print(len(users))

users.append('Elsa')
print(users)

users+= ['Json']
print(users)
# these two is the same
users.extend(['jim', 'bach'])
print(users)

users.insert(0,'bob')
print(users)
#add not replace 
users[1:1] = ['leu', 'alex']
print(users)

users.remove('bob')
print(users)

users.pop()
print(users)

del users[1:3]
print(users)

# del users
# print(users)

users.sort()
print(users)
# key is to turn all of them to lower and then sort
users.sort(key=str.lower)
print(users)

nums = [1,2,3,4,5,7,1,2,5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums,reverse=False))
print(nums)
# copy from the base
numscopy = nums.copy()
mycopy = list(nums)
copycopy = nums[:]

mylist = list([1, "neil", True])
print(mylist)

#TUPLE
newtupple = (1,2,3,3,3)
anothertupple = tuple((1,2,3))
print(type(newtupple))
print(anothertupple)
print(type(anothertupple))

newlist = list(newtupple)
newlist.append(10)
newtuple = tuple(newlist)
print(newtuple)

print(newtuple.count(3))
print(newtuple.index(3))
# the *parameter in tuple is the one include all the rest element, it can be in the middle
(one, two, *three) = newtuple
print(one)
print(two)
print(three)


