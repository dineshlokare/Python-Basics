#Elif Operations

savings = float(input('Enter you savings:'))
if savings == 0:
    print('sorry no savings')
elif savings < 500:
    print('well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome sir')
else:
    print('thank you!')
    
#####################################################
#to increase font size > tools> preferences> appreance> size of Font
#####################################################

#LOOPs
#While Loop

count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1
    
#########################################################
#For Loop
#Loop over a set of values in a range

print('print out values in a range')
for i in range(2, 10):
    print(i)
    print('Done')
    
    #whenever we use 'range' in for loop it not consider last value

###############################################################

print('only print code if all iterations completed')
num = int(input('Enter a number to check for:'))
for i in range(0,16):
    if i == num:
        break
    print(i)
print('Done')

###########################################

#Now use an 'anonymous' loop variable

#vertical
for _ in range(0,10):
    print('.', end='')
    print()

#horizontal
for _ in range(0,10):
    print('.', end='')
    
######################################    
#Break loop statement

print('Only print code if all iterations completed')
num = int(input('Enter a number:'))
for i in range(0,6):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')

#location changed

print('Only print code if all iterations completed')
num = int(input('Enter a number:'))
for i in range(0,6):
    if i == num:
        break
    print(i,' ', end='')
    print('Done')
    
########################################################

# Q. Python program to print odd numbers in given range

start, end = 4, 19

#iterating each number in list
for num in range(start, end + 1):
    
    # checking condition
    if num % 2 !=0:
        print(num, end = " ")
        
##########################################################

start, end = 4, 19

#iterating each number in list
for num in range(start, end + 1):
    
    #checking condition
    if num % 2 == 0:
        print(num)

#################################################
#python program to print all even numbers in range

for even_numbers in range(5,15,2):
    #here inside in range function first no. denotes starting
    #second denotes end and
    #third denotes the interval
    print(even_numbers, end=' ')


start = int(input('Enter the start of range: '))
end = int(input('Enter the end of range:'))

# iterating each number in list
for num in range(start, end + 1):
    
    #checking condition
    if num % 2 == 0:
        print(num, end=' ')
        print()
#write code for find prime numbers in given range
#leap year
#whether you string is palindrome
#mario pyramid
#ASSIGNMENT 1

#-------------Prime numbers-------------#

start = int(input('Enter the start range:'))
end = int(input('Enter the end range:'))
print('Prime numbers in the range are:')
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
               break
        else:
            print(num)

#----------------To Check Leap Year----------------------#

year = int(input('Enter year to be checked:'))
if(year%4==0 and year%100 !=0 or year%400==0):
    print("The year is a leap year!")
else:
    print('The year is not a leap year')

#--------------palindrome string------------------------#

s=input("enter the string:")
t=s[::-1]
print(t)
if(t==s):
    print("it is palindrome")
else:
    print("it is not palindrome")

#main string = reverse string then it is said to be palindrome

#-------------mario pyramid---------------------#
#asked in interview

for i in range(5):
    for j in range(i + 1):
        print("#", end=" ")
    print()
"""
# 
# # 
# # # 
# # # # 
# # # # # 
 """
n=int(input("enter the number:"))
for i in range(n):
    for j in range(n-i):
        print("#",end=" ")
    print()

n=int(input("Enter the number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
    
n = 5
for i in range(1, n+1):
    spaces = ' ' * (n - i)
    stars = '*' * (2*i - 1)
    print(spaces + stars)

#global variables

x="Awesome"
def my_function():
    print("python is "+x)
my_function()

#global and local variables

x="Awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)


x=range(6)
print(type(x))

x={"name":"dinesh", "age":22}
print(type(x))

###################################################

# we can't add string with integer

str1="hello"
str2=2
str3= str1 + str2

#can only concatenate str (not "int") to str

#########################################################

#string
#if you want multiple strings

x="""This is python. It is very powerful"""
print(x)

#################################################
#string slicing

x="This is python" #indexed from 1,2,3... towards right
print(x[2:6])

print(x[:3]) #slice from start
print(x[4:]) #slice from end

#negative indexing 
x="This is python"  #indexed from -1,-2,-3...from right to left
print(x[-5:-2])

#######################################################
#Modify String

x="I am Thor"
print(x.upper())
# for lower print(x.lower())
##############################################

#remove the white space, removes white space from initial to end

x=" This is python"
print(x.strip())

#replacing

x="Hello world"
print(x.replace("Hello","Gello"))
####################################
#use of split whic replaces white space/or ,

x="hello,world"
print(x.split(",")) #separator is comma

#after that vectorization is done>> applied to model>> ML is done

##########################################################################

x="Hello World"
print(x.split(" ")) #separator is space

x="Hello World"
string1=x[::-1]     #meaning of :: start to end reverse
print(string1)

x="this is python and it is powerful" 
print(x.find("and"))                     #to find particular string

x="hello"
y="dinesh"
print(x+" "+y)  #concatnation

x=32
y="my name is anthony"
#print(x+y)
#it will give error 
print(f"my name is anthony and my age is {x}")

quantity = 3
item_no = 54
price = 80
print(f"I want {quantity} and item no. is {item_no}, its price is {price}")

# f-string is used here

my_order="I want {} pieces and item number is {}, its price is {}"
#my_order="I want {0} pieces and item number is {1}, its price is {2}"
#we can also have position of arguments
print(my_order.format(quantity, item_no, price))

#################################################################

#the escape character allows you to use double quotes when you normally would
text="this is fun fair and it has got big \"round rigo\""
print(text)

#operator precedence
print(3*3+3/3-3)

#----------------------Rule for mathematical operatons------------------#

#PEMDAS
#P: Paranthesis
#E: Exponential
#M: Multiplication
#D: Division
#A: Addition
#S: Substraction





