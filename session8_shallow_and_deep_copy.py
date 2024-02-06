#---------------------Shallow copy and Deep copy---------------------------#

#Assignment Operation

list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)

# >>>>>>>>>>>>>>>>>>>>>>>>>>> shallow copy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

#One level deep. Modifying on level 1 does not affect the other list.
#Use copy.copy(), or object-specific copy functions

import copy

list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

# not affects other list
list_b[0]=-10
print(list_a)
print(list_b)

#but with nested objects, modifying on level 2 or deeper does affect the other

import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

# affects the other!
list_a[0][0]=-10
print(list_a)
print(list_b)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Deep copy <<<<<<<<<<<<<<<<<<<<<<<<<<<< #

#Deep copy
#full independent clones are created
#use copy.deepcopy()

import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

# not affects the other!
list_a[0][0]=-10
print(list_a)
print(list_b)

#################################################################

""" write a pyhton program to create an iterator from several
    iterables in a sequence and display the type and elements of the
    the new iterator
"""

# Concept -> itertools.chain

from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#List
result=chain_func([1,2,3],['a','b','c','d'],[4,5,6,7,8,9])
print('Type of the new iterator:')
print(type(result))
print('Elements of the new iterator')
for i in result:
    print(i)
    
#same for tuples

from itertools import chain
def chain_func(lst1,lst2,lst3):
    return chain(lst1,lst2,lst3)
#List
result=chain_func((1,2,3),('a','b','c','d'),(4,5,6,7,8,9))
print('Type of the new iterator:')
print(type(result))
print('Elements of the new iterator')
for i in result:
    print(i)

###############################################################

"""write a python program that generates the runnig product
of elements in an iterable"""

from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)

#list
result = running_product([1,2,3,4,5,6,7])
print('Running product of a list:')
for i in result:
    print(i)

#tuple

from itertools import accumulate
import operator
def running_product(lst):
    return accumulate(lst,operator.mul)

result = running_product((1,2,3,4,5,6,7))
print('Running product of a list:')
for i in result:
    print(i)

##################################################################

"""write a python program to construct an infinite iterator that
    returns evenly spaced values starting with a specified number and
    step
"""
import itertools as it
start = 10
step = 1
print('The starting number is',start,'and step is',step)
my_counter=it.count(start,step)
#following loop will run for ever
print('The said function print never-ending items:')
for i in my_counter:
    print(i)

#this is used in data augmentation

##############################################################

""" write a python prorgram to generate an infinite cycle 
    of elements from an iterable.
"""

import itertools as it
def cycle_data(iter):
     return it.cycle(iter)
 #following loops will run for ever
 #list
result = cycle_data(['A','B','C','D'])
print('The said function print never-ending items:')
for i in result:
    print(i)
    
#string
import itertools as it
def cycle_data(iter):
     return it.cycle(iter)
result = cycle_data("Python itertools")
print("The said function print never-ending items:")
for i in result:
    print(i)

#########################################################
""" write a python program to make an iterator that drops
    elements from the iterable as soon as an element is 
    positive number.
"""

import itertools as it
def drop_while(nums):
    return it.dropwhile(lambda x:x<0, nums)
nums = [-1,-2,-3,4,-10,2,0,5,12]
print("original list:", nums)
result = drop_while(nums)
print('Drops elements from the iterable when a positive number arises\n',list(result))










