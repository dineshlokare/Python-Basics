#Returning Dictionary
#key value pair

def build_person(first_name, last_name):
#Return a dictionary of information about a person.
    person = {'first': first_name, 'last': last_name}
    return person
musician=build_person('Dinesh', 'lokare')
print(musician)

##########################################################
#Passing List

def greet_users(names):
    #print a simple greeting to each user in the list.
    for name in names:
        msg = f"hello, {name.title()}!"
        print(msg)
usernames = ['dinesh', 'amey', 'amar']
greet_users(usernames)

################################################################
#Passing an Arbitrary number of arguments

def make_pizza(*toppings):
    #print the list of toppings that have been requested
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#Now we can replace the print() call with a loop that runs through the 
#list of toppings and describes the pizza being ordered:

    
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:    
        print(f"- {topping}")
        
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

###############################################################
#Mixing Positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    print(f"\nMaking a {size} -inch pizza with the following toppings:")
    for topping in toppings:    
        print(f"- {topping}")
        
make_pizza(10,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

################################################
#creating seperate file/module of specific name 
#and to import that file to existing file

import pizza

pizza.make_pizza(10,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')
#interview question on this

####################################################

#importing specific functions

from pizza import make_pizza
make_pizza(10,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
##############################################################

#Using as to Give a Functions as Alias
#here function with large names is replaced with small names
#Alias name to function

from pizza import make_pizza as mp
mp(10,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')

##############################################################

#Using as to Give a Module an Alias
import pizza as p
p.make_pizza(10,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')
 
####################################################

#Importing all functions in a Module
from pizza import *
make_pizza(10,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')

#######################################################
#Scope of variable

x=x+1
x=6
print(x)

"""you cannot reference a variable
until it has been assigned a value."""

#corrected
x=6
x=x+1
print(x)
########################################################

"""Lamda function / Anonymous Function"""
#interview question

def add(a,b,c):         #function without lambda function
    sum=a+b+c
    return sum
print(add(4,5,3))

add=lambda a,b,c:a+b+c  #-> name of func=lambda arguments:business logic
add(4,5,3)

def mul(a,b,c): #function without lambda function
    mul=a*b*c
    return mul
print(mul(4,5,6))

mul=lambda a,b,c:a*b*c        #function with function
mul(4,5,6)

##################################################
#if arbitrary arguments present

val=lambda *args:sum(args) # *args-> arbitrary arguments/keyword arguments
val(1,2,3,4,5,6)
val(1,2,3,4,5,6,7,8,9)

########################################
def person(name, *data): # *data-> positional argument
    print(name)
    print(data)
person('navin',23,'mumbai','local man')
##############################################

def person(name, **data):       #**data-> keyword argument
    print(name)
    print(data)
person(name='dinesh', age=22, place='parli', mob_no=83433)

##########################################################3

def person(name, **data): #**data -> keyword argument
    print(name)
    for i,j in data.items():  #items() -> for key's values
        print(i,j)
person('Navin', age=34, place='mumbai', mob_no=232422)

##################################################

val=lambda **data:sum(data.values())
val(a=2,b=5,c=7,d=10)

################################

max=lambda a,b:x if (a>b):
    print(max(1,2))
# is going to give error

max=lambda a,b:a if (a>b) else b
print(max(1,2))

x = lambda a : a + 10
print(x(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
