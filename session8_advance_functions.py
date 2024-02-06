#---------------------zip Function--------------------------#

#imp question interview
#use of zip function
name=['dada','mama','kaka']
info=[322,343,5322]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#with the mistmatch list 
name=['dada','mama','kaka','baba']
info=[322,343,5322]
for nm,inf in zip(name,info):
    print(nm,inf)

#it will not display excess mismatch item in name
#i.e baba
#this is disadvantage
###################################################################

#zip longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[322,343,5322]
for nm,inf in zip_longest(name,info):
    print(nm,inf)  

#it will take care of extra parameter of list
#it will add none value to them
#zip functions will be used at NLP application
##################################################################

#use of fill value instead None

from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[322,343,5322]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)  

##########################################################

#use all(), if all the values are true then it will produce output
#this function is going to be used in feature engineering

list=[2,3,6,8,9]  
if all(list):
    print('all values are true')
else:
    print('useless')
    
#if zero it shows useless 
list=[2,3,6,8,0,9]  
if all(list):
    print('all values are true')
else:
    print('useless')

############################################################
#Use of any if any one non zero value

list=[0,0,0,4,0]  
if any(list):
    print('It has some value')
else:
    print('useless')
    
list=[0,0,0,0]  
if any(list):
    print('It has some value')
else:
    print('useless')
    #all values were zero

#########################################################

#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

#now let us start from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))

######################################################
#cycle()
#suppose you have repeated tasks to be done then you can use this method
###########################################################
#repeat()

from itertools import repeat
for msg in repeat('keep patience',times=3):
    print(msg)

############################################
#combinations()

from itertools import combinations
player=['john','joni','janardhan']
for i in combinations(player,2):
    print(i)

"""
Output:
    
    ('john', 'joni')
    ('john', 'janardhan')
    ('joni', 'janardhan')
"""
#######################################################
#permutations()

from itertools import permutations
player=['john','joni','janardhan']
for i in permutations(player,2):
    print(i)
    
#################################################
#product()

from itertools import product 
team_a=['virat','rohit','bumrah']
team_b=['pandya','manish','dhoni']
for a in product(team_a, team_b):
    print(a)
    
####################################################
#filter()

age=[23,22,15,20,21]
adults=filter(lambda age:age>=18, age)
print([age for age in adults])


















    
    
    
    
    
    
    
