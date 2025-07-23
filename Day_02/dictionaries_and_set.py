# DICTIONARIES
band = {
    "key" : "word",
    "time" : "shift", 
    "meow" : "meo"
}

band2 = dict(key = "word", meow = "meo", time = "shift")

print(band)
print(band2)
print(type(band))
print(type(band2))
print(len(band))

#Access Item
print(band2["meow"])
print(band.get("key"))

#List all key
print(band.keys())

#List all values
print(band.values())

#List all pairs
print(band.items())

#verify if the key exits
print("key" in band)
print("triangle" in band)

#change value
band["key"] = "meow"
band.update({"meow": "meow"})
band.update({"dog": "gau"})
band["monkey"] = "hihi"
print(band)


#remove Items

band.pop("dog")
print(band)
band.popitem()
print(type(band))
print(type(band.popitem())) #its a tuple

#delete items
print(band)
del band["time"] 
print(band)

band["monkey"] = "hihi"
print(band2)
band2.clear()
print(band2) #clear all the elements in dict
del band2 #remove band2 attribute
#print(band2) it's not valid 

#Copy dict
band2 = band # copy the reference not the value
del band2 
print(band)
band2 = band.copy() #copy the value
band3 = band.copy() #also the value

#Nested dictionary in dictionary
overallband = {
    "member1" : band, 
    "member2" : band2,
    "member3" : band3
}

print(overallband["member1"]["monkey"]) #access to member dict

#Set
nums = {1,2,3,4}
nums2 = set((1,2, 3, 4))
print(nums)
print(nums2)
print(type(nums2))
print(len(nums))

#True is a dupe of 1 and False is a dupe of zero
nums3 = {1, True, 0, False, 3, 4, 5}
print(nums3)

#check if a value is in set
print(3 in nums)

#Add a new element to set
nums.add(8)
print(nums)

#Add elements to a set 
#Update can be use with tuple, list, set, dict
newlist = [6,7,8,9]
nums.update(newlist)
print(nums)
nums.update(nums3) 
print(nums)

#Merge two set to become one set
one = set((1,2,3))
two = set((4,5,67))
mynewset = one.union(two)
print(one)
print(type(one))

#Keep only the duplicate 
one = set((1,2,3))
two = set((4,2,3))
one.intersection_update(two)
print(one)
print(two)

#keep everything except the duplicate 
one = set((1,2,3))
two = set((4,2,3))
one.symmetric_difference_update(two)
print(one)