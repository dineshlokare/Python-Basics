# Python collections types: Tuples, List, set and Dictionary

"""--------------------creating tuples--------------- """

tup1=(1,3,5,7)
#Accessing elements of a tuple
print(f'tup1[0]:\t {tup1[0]}')
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

""" Tuples are used to store multiple items in single variable
    A tuple is a collection which is ordered and immutable 
"""

# Tuples can hold different datatypes
tup2 = (1, 'john', True, -23.34)
print(tup2)

#iterating over tuples
tup3=('apple','orange','plum','apple')
for x in tup3:
    print(x)
    
#Tuple related functions
""" you can also find length of tuple"""
len(tup3)

#you can count how many times a specified value"
#appears in tuple

tup4 = ('apple','orang','plum','apple')
#tuples allow duplicates
tup4.count('apple')
#you can also find out the (first) index of a value in a tuple:
print(tup4.index('apple'))
print(tup4.index('plum'))

#checking if an element exists
if 'orange' in tup3:
    print('orange is in tuple')

#nested tuples
tuple1 = (1,3,5,7)
tuple2 = ('john','Denise','phoebe','Adam')
tuple3 = (43, tuple1, tuple2, 5.5)
print(tuple3)


#It is not possible to add or remove
#Elements from a Tuple; they are immutable;
#Elements cannot be changed ->immutable

#####################################################

#------------------------Lists Section--------------------#

#Lists are mutable, indexed, ordered
#add or delete elements -> mutable

#creating lists
lst1 = ['john','paul','george','ringo']
#As with tuples we can have nested lists and lists containgin diffn
#elements.

lst1 = [1,43,True]
lst2 = ['apple','orange', 31]
root_list = ['john', lst1, lst2, 'denise']
print(root_list)

#Acessing elements from list
lst1 = ['john','paul','george','ringo']
print(lst1[-1])
print(lst1[0])
print(lst1[-2])
print(lst1[1:3]) #range -> goes upto 2 only
print(lst1[:3])
print(lst1[1:])
print(lst1[0:3])

#Adding to a list

lst1 = ['john','paul','george','ringo']
lst1.append('pete')
print(lst1)

#you can also add all the items in the list
#to another list. There are several options

lst1 = ['john','paul','geroge','pete']
print(lst1)
lst1.extend(['albert','amrya'])
print(lst1)
#here we can use extend()

#inserting into a list
a_list = ['Adele','Madonna','Cher']
print(a_list)
a_list.insert(1,'paloma')
print(a_list)

#List Concatenation

lst1 = [1,2,3]
lst2 = [4,5,6]
#lst3 = lst1 + lst2
#print(lst3)
print(lst1 + lst2)

#Removing from a list
another_lst = ['gary','mark','robbie','jason','howard']
print(another_lst)
another_lst.remove('robbie')
print(another_lst)

#pop method
#it removes an element from the list
#however, it differs from the remove()
#method in two ways:
#It takes an index which is the index of the item
another_lst = ['gary','mark','robbie','jason','howard']
print(another_lst)
another_lst.pop(2)
print(another_lst)

#inserting in the list
a_list = ['adele','madonna','cher']
print(a_list)
a_list.insert(1,'danny')
print(a_list)


""" Q1 take 5 no in a list find min and max from them
    Q2 take 5 string in list and make it reverse
    Q3 take 10 no in list write script to search for a value
    Q4 take 10 nos in the list insert some duplicates nos, write 
    script to find duplicates
    Q5 take vowels in the list and non vowels letters, find out the
    total no of vowels in the list
"""
# Q1
lst = [1,3,243,5,6]
lst.sort()
a=lst[4]
b=lst[0]
print("Max:",a)
print('Min:',b)

#Q2
lst_string = ['dinesh','tushar','vinit','sarvesh','abhi']
lst_string.reverse()
print("Reversed string: ",lst_string)

#Q3
numbers = [11,12,23,43,32,45,18,22,44,76]
num = int(input('enter you number to be search: '))
if num in numbers:
    print(f'{num} number is present') 
else:
    print('number is not present')
    
#Q4
numbers=[11,12,11,32,43,54,66,75,66,32]
number=[]
for num in numbers:
    if numbers.count(num)>=2:
        if number.count(num)==0:
            number.append(num)
print(number)

#Q5
letters = ['a','e','k','l','m','q','t','r','s','j']
vowel=[]
count=0
for letter in letters:
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        count+=1
        vowel.append(letter)
print(count)
print(vowel)
