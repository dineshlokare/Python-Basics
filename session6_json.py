#Storing Data

"""
JSON (JavaScript Object Notation):- format was originally developed for Java
Using JSON json.dump() 
Many of your programs will ask users to input certain kinds of information.
You might allow users to store the information users provide in data
structures such as lists and dictionaries.
When users close a program, you'll almost always want to save the 
information they enetered.
A simply way to do this involves storing your data using the json module.
"""

import json

numbers = [2,3,4,5,6,7]
filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)

##################################

import json

username = input('What is you name?')
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username,f)
print(f"We'll remember you when you come back, {username}!")

#Now let's write a new program that greets 
# a user whose name has already been stored

# Load the username, if it has been stored previously
# otherwise, prompt for the username and store it

import json

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    
    username = input('What is you name?')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username,f)
    print(f"We'll remember you when you come back, {username}!")
else:
    print(f'Welcome back, {username}!')
    
    
