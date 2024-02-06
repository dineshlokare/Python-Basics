

###############----------LIST COMPREHENSION-----------################
lst=[]
for i in range(0,20):
    lst.append(i)
print(lst)

#same code using list comprehension
lst=[i for i in range(0,20) ]
print(lst)

#capitalize()-> make 1st letter of word capital
lst=["kaka","mama","dada"]
lst1=[i.capitalize() for i in lst]
print(lst1)

#if in list comprehension
#business logic is on left side of for
#if condition is on right side of for
lst=[i for i in range(10) if i%2==0]
print(lst)

#calling function in list comprehension
def even(num):
    if num%2==0:
        return num
lst=[i for i in range(10) if even(i)]
print(lst)

###assignments
#all list assignments perform using list comprehension

#nested loop in list comprehension
lst=[f"{x}{y}" for x in range(3) for y in range(3)]
print(lst)
#O/p -> ['00','01','02','10','11','12','20','21','22']

##############################################
#SET COMPREHENSION
s1={i for i in range(3)}
print(s1)


############################################
#DICTIONARY COMPREHENSION
dict1={x:x*x for x in range(3)}
print(dict1)

dict1={x:x for x in range(10) if x%2==0}
print(dict1)


############################################
#Generator ->can return multiple values
#instead of using return keyword it uses yield keyword

#gen=(x for x in range(3))
#tuple comprehension will create object
#object is always is in format of 
#<generator object <genexpr> at 0x000001ACDCE97440>
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)
#when you are going to use tuple comprehension ,one object will be create
#you can access values of that object using for loop

#to iterate in object of gen 
#we can use next() function , it will iterate over object
gen=(x for x in range(3))
print(next(gen))
next(gen)
next(gen)
next(gen)
next(gen)


#function returning multiple values
def range_even(end):
    for i in range(0,end,2):
        yield i
for num in range_even(6):
    print(num)

#instead of using for loop we can use our own generator
gen=(range_even(6))
next(gen)
next(gen)
next(gen)
next(gen)


########################################
#chaining of generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
        
def hide(itr):
    for ele in itr:
        yield ele* '*'

passwords=["not-good","give'm-pass","001100=100"]
for i in hide(lengths(passwords)):
    print(i)
    
    
####################################
#enumerate
lst=["Milk","bread","Egg"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")    
    
#same code using enumerate
lst=["Milk","Egg","Bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
#################################################

"""Password Generator"""

import string              #python library  
    
#pick the adjectives

adjectives = ['sleepy','slow','smelly','wet','fat','red','yellow','green',
              'blue','purple','fluffy','white','proud','brave']
#pick the nouns

nouns = ['apple','dinesh','dinosour','ball','toaster','goat','dragon',
         'hammer','duck','panda']

#pick the words
import random               #python library to choose randomly


adjective = random.choice(adjectives)
noun = random.choice(nouns)
    #select a number
number = random.randrange(0,100)
    #select a special character
special_char = random.choice(string.punctuation)
    #Create a new secure password
password = adjective + noun + str(number) + special_char
print('you new password is : %s' % password)

def lengths(itr):
        for ele in itr:
            yield len(ele)
            
def hide(itr):
        for ele in itr:
            yield ele* '*'
for i in hide(lengths(password)):
        print(i,end="")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        