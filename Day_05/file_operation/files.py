# r = read 
# w = write 
# a = append 
# x = create 

# read is error if the file doesn't exist 

file_names = open('names.txt', 'r') 
# print(file_names.read())  # read the entire file content
# print(file_names.read(10))
print(file_names.readline())  # read the first line
print(file_names.readline())  # read the first line

for line in file_names:
    print(line)  # print line 
    
file_names.close()  # close the file after reading

try: 
    file_names = open('more_names.txt', 'r')
    print(file_names.read())
except Exception as error: 
    print(error) #file not found error
finally:
    file_names.close()

# append mode
file_names = open('names.txt', 'a')  # open in append mode
file_names.write("Long")
file_names.close()

file_names = open('names.txt', 'r')  # re-open to read the updated file
print(file_names.read())
file_names.close()

# write mode (deletes existing content, and rewrites all of them)

#two ways to create a file 

# create a new file using write mode 
file_names = open('new_names.txt', 'w')  # create a new file
file_names.close()
#create a new file using x mode, but it return error if the file already exists so using os to check if the file exists
import os
if not os.path.exists('meow_names.txt'):
    file_names = open('meow_names.txt', 'x')  # create a new file
    file_names.close()
    
# delete a file

# avoid deleting a file that doesn't exist
if os.path.exists('meow_names.txt'):
    os.remove("meow_names.txt")  # delete the file
else: 
    print("The file does not exist")
    
with open("names.txt", "r") as file_names:  # using with statement to automatically close the file
    content = file_names.read()  # read the file content

print(type(content))  # content is a string

print(content)  

# show items 