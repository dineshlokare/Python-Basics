
#-------------------Assignment List Comprehension-------------------#


""" Find all of the numbers from 1-1000 that are divisible by 7"""

div7 = [ n for n in range(1,1000) if n % 7 ==0]
print(div7)

########################################################

""" find all of the numbers from 1- 1000 that have 3 in them"""

three = [ n for n in range(1,1000) if '3' in str(n)]
print(three)

#############################################################

""" count the number of spaces in string """

some_string = 'the slow solid, squid swam sumptuously through'

spaces = [s for s in some_string if s==' ']
print(len(spaces))

#########################################################

"""create a list of all consonants in the string """
""" Yellow Yaks like yelling and yawning and yesterday
 they yodled while eating yuky yams"""

sentence = "Yellow Yaks like yelling and yawning and yesterday"

result = [letter for letter in sentence if letter not in 'a,e,i,o,u," "']
print(result)

########################################################

""" Find the common numbers in two lists (without using tuple or set)"""

list_a =[1,2,3,4]  # taken 'a' in list_a and compared with list_b
list_b =[2,3,4,5]

common = [a for a in list_a if a in list_b]
print(len(common))
print(common)

########################################################

""" Get only the numbers in a sentence like 'In 1984 there were 13
    instances of a protest with over 1000"""
#important question
#extraction of number from a give string using list comprehension

sentence = 'In 1984 there were 13 instances of a protest with over 1000'

words = sentence.split()

result = [number for number in words if not number.isalpha()]
print(result)

#isalpha() -> methods returns True if all the characters are alphabet
#             letters


###############################################################

""" Given numbers = range(20) we have to print even for even nos.
    odd for 'odd' for odd nos."""

result=[]
for n in range(20):
    if n % 2 ==0:
        result.append('even')
    else:
        result.append('odd')
print(result)

#in list comprehension if else condition occurs write it to left of
# for loop

result =['even' if n % 2 == 0 else 'odd' for n in range(20)]
print(result)

#################################################################

"""  produce a list of tuples consisting of only
    the matching numbers in there lists list_a=[1,2,3,4,5,6,7,8,9]
    list_b=[2,7,1,12]
"""
list_a=[1,2,3,4,5,6,7,8,9]
list_b=[2,7,1,12]
#creating tuples in the list (a,b) a from list_a & b from list_b
result=[(a,b) for a in list_a for b in list_b if a == b]
print(result)

#home assign take two sentence and print same words in tuple list
#first split

sent1 = 'I am computer engineer'
sent2 = 'I develope softwares in computer'

w1 = sent1.split()
w2=sent2.split()

result=[a for a in w1 if a in w2]
print(result)

################################################################

"""
    Find all of the words in a string that are less tha 4 letters
"""

sentence='On a summer day Ramnath sonar went swimming in the sun and his red skin stung'

examine=sentence.split()

result=[word for word in examine if len(word)<=4]
print(result)

####################################################################

"""
    Write a python program to print a specified list
    after removing the 0th , 4th and 5th elements.
"""
color=['Red','Green','White','Black','Pink','Yellow']
color=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
#enumerate show key:value here index:value

#############################################################
"""
    Write a python program that creates a generator function 
    that yields cube for numbers from 1 to n and takes n from user
"""

def cube_generator(n):
    for i in range(1,n+1):
        yield i ** 3
        
#Accept input from the user
n = int(input('Input a number: '))

#create the generator object
cubes = cube_generator(n)

#iterate over a generator
print('Cubes of numbers from 1 to',n)
for num in cubes:
    print(num)
    
#######################################################################3
"""
    write python program to implement a generator that generates
    random numbers within  a given range
"""
import random

def random_number_generator(start,end):
    while True:
        yield random.randint(start,end)
        
#Accept input from the user
start=int(input('Input for the start: '))
end=int(input('Input for the end: '))

#create the generator object
random_numbers=random_number_generator(start,end)

print('Random numbers from {start} and {end} are: ')
for _ in range(10):
    print(next(random_numbers))

################################################################
#we you are going for multi dimensional array
"""
[[square brackets]] -> two dimensional vector
[[[square brackets]]] -> Three dimensional vector
[[[[square brakets]]]] -> 4D

"""
""" 
    python program to generate a 3*4*6 3D array whose each element is *
"""
array=[[['*' for col in range(6)]for col in range(4)]for row in range(3)]
print(array)

####################################################################
"""
    write a python program to print the numbers of a specified
    list after removing even numbers from it
"""
num=[1,2,3,4,5,6,7,8,9,10]
result=[n for n in num if n % 2 != 0]
print(result)



