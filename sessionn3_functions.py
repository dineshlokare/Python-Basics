#--------------------------------Functions--------------------------------#

def prime_num(num):             #function definition
    for i in range(2,num):
        if (num % i == 0):
            return"The number is not prime"
            break
    return"the number is prime"
print(prime_num(12))        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#displaying a simple greeting

#function without argument
def greet_user():
    print("Hello!")
greet_user()

#passing information to a function
def greet_user(username):
    print(f"Hello {username}!")
greet_user("Sanjivani AI")

###################################################

#Arguments and parameters
#The variable username in the def of greet_user is an example of a
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('lion', 'simba')
#order matter in positional argument
 
#############################################

#default values

def describe_pet(animal_type, pet_name='simba'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}.")
describe_pet('lion')

#when you are defining functions with default values, while calling that
#function it is not necessary to pass this argument

##############################################
#Avoiding Argument Errors
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('Dog','Rocky')

#####################################################################
#ASSIGNMENTS

#Q1. Create a prgroam using maths and f string and tell us how many days,weeks
#and months we have left if we will live until 80 years.



#roller coaster problem code by me

h = int(input("Enter you height in cm: "))   
if h >= 120:
    a = int(input("Enter your age:"))
    if(a<12):
        print('ticket is 10Rs')
    elif (a<=18):
        if (a>=12):
            print('ticket is 15Rs')
        else:
            print('ticket is 20Rs')
            
    else:
        print('tikcet is 50Rs')
else:
    print('you are not eligible to ride')


#Code By sir

print('welcome to roller coaster')
height = int(input('please enter your height in cm: '))
bill=0
if height>=120:
    print('you are eligible for ride')
    age=int(input('please enter your age: '))
    if age<12:
        print('child tickets are $5')
        bill=5
    elif age<=18:
        print('youth tickets are $7')
        bill=7
    else:
        print('Adult tickets are $12')
        bill=12
    want_photo=input('Do you want photo Y or N: ')
    if want_photo == 'Y':
        bill+=3
        print(f"you total bill will be {bill}")
    else:
        print(f"your total bill ${bill}")
else:
    print("sorry you need to grow taller")
    
################################################################
#List of users
users = ["admin","employee","manager","worker", "staff"]
for user in users:
    if user=="admin":
        print("Hello admin, would you like to check status report?")
    elif user=="employee":
        print("Hello employee")
    elif user=="manager":
        print("hello Manager")
    elif user=="worker":
        print("Hello worker")
    else:
        print("Hello welcome!")
        
###############################################################
        
#Password Picker code

import string              #python library  
    
#pick the adjectives

adjectives = ['sleepy','slow','smelly','wet','fat','red','yellow','green',
              'blue','purple','fluffy','white','proud','brave']
#pick the nouns

nouns = ['apple','dinesh','dinosour','ball','toaster','goat','dragon',
         'hammer','duck','panda']

#pick the words
import random               #python library to choose randomly

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    #select a number
    number = random.randrange(0,100)
    #select a special character
    special_char = random.choice(string.punctuation)
    #Create a new secure password
    password = adjective + noun + str(number) + special_char
    print('you new password is : %s' % password)
    #Another one
    response = input('would you like to generate another  passoword? y or n: ')
    if response == 'n':
        break

#####################################################################
#   Write python code that determine whether or not
#   a password strong. we define strong password if it follows
#   following conditions
#   1. it  must have at least 8 characters
#   2. it must have at least one uppercase letter
#   3. one lower case letter

def checkPassword(password): 
    has_upper = False
    has_lower = False
    has_num = False
#check each character in the password ans see match
#requirements meets
    for ch in password:
        if ch>="A" and ch<="Z":
            has_upper=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="0" and ch<="9":
            has_num=True
    if len(password)>=8 and has_upper and has_lower and has_num:
        return True
    else:
        return False
p=input("Enter a Password: ")
if checkPassword(p):
    print("Strong Password")
else:
    print("Weak Password")

#######################################################################

#Q1. Create a prgroam using maths and f string and tell us how many days,weeks
#and months we have left if we will live until 80 years.

print("What is your today age")
years_today=input("Years: ")
months_today=input("months: ")
days_today=input("Days: ")
total_days_today=int(years_today)*365+int(months_today)*30+int(days_today)
print(f'Your total age in today in days {total_days_today}')
print('Let us assume you are expected to live 90 Years')
total_days_to_live=90*365
remaining_days_to_live=total_days_to_live-total_days_today
print(f'Your remaining life in days {remaining_days_to_live}')

#####################################################################3

print('Welcome to the pizza hut')
bill=0
pizza_size=input('Enter the size of pizza: S,M,L - ')
if pizza_size=='S':
    print('cost is $15')
    bill=15
elif pizza_size=='M':
    print("cost is $20")
    bill=20
elif pizza_size=='L':
    print('cost is $25')
    bill=25
add_pepp=input("do you want pizza with pepproni Type y or n:")
if add_pepp=='y' and pizza_size=='S':
        bill+=2
        print(f"your total bill is {bill}")
elif add_pepp=='y' and pizza_size=='M':
        bill+=3
        print(f"your total bill is {bill}")
elif add_pepp=='y' and  pizza_size=='L':
        bill+=3
        print(f"you totol bill is {bill}")
extra_cheese=input("do you want to add extra cheese? type y or n: ")
if extra_cheese=='y':
    bill+=1        
    print(f"you total bill is ${bill}")
    
    
    
