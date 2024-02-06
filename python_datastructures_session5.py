#-----------------------SET-----------------------------#

#creating a set
basket = {'apple','orange','apple','pear','orange','banana'}
print(basket)
#after running this code it won't allow duplicate entities -> set

#accessing elements in a set

for item in basket:
    print(item)
    
#Adding items to set
basket = {'apple','orange','banana'}
basket.add('apricot')
print(basket)

#if you want to add more than on item to a set you can use the update
basket = {'apple','orange','banana'}
basket.update(['apricot','pear','mango',])
print(basket)

#Obtaining the length of set
basket = {'apple','orange','apple','pear','orange','banana'}
print(len(basket))

#Obtaining the Max and Min Values in a set
basket2 = {23,43,67,12,456}
print(max(basket2))
print(min(basket2))

#Removing an item
basket = {'apple','orange','apple','pear','orange','banana','apricot'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket) 

#set operations
s1 = {'apple','orange','banana'}
s2 = {'grapefruit','lime','banana'}
print('Union: ', s1 | s2)
print('Intersection: ', s1 & s2)
print('Difference: ', s1 - s2)


#-----------------------DICTIONARY-----------------------------#


#A dictionary is a set of associations
# between a key and a value that is unordered
# changeable (mutable) and indexed

capitals = { 'Maharashtra':'Mumbai', 'Gujrat':'Ahmadbad','UP':'Lucknow',
            'Karnataka':'Bangalore','Andhrapradesh':'Hyderabad'}

print(capitals)

#Acessing items via key

print('Capital[Maharashtra]: ', capitals['Maharashtra'])

#Adding a New Entry
capitals['West Bengal'] = 'Kolkata'
capitals

#Changing a Keys value
capitals['Gujrat'] = 'Gandhinagar' #value changed
capitals

#Removing an entry
capitals.pop('Karnataka') #key is popped
print(capitals)
del capitals['UP'] # key is removed 
print(capitals)

#Iterating over keys
capitals = { 'Maharashtra':'Mumbai', 'Gujrat':'Ahmadbad','UP':'Lucknow',
            'Karnataka':'Bangalore','Andhrapradesh':'Hyderabad'}

#This imp most of time it is required
for states in capitals:
    print(states, end=', ')
    print(capitals[states])

#values, keys and Items
print(capitals.values())
print(capitals.keys())
print(capitals.items())

#changing key membership
print('Karnataka' in capitals)
print('Bihar' not in capitals)

#obtaining the lenght of Dictionary
print(len(capitals))

#Dictionaries can have values in tuple
seasons = {'summer': ('Feb','Mar','Apr','May'),
           'Rainy': ('June','July','August','Sept'),
           'Winter': ('Oct','Nov','December','January')}
print(seasons['Rainy'])
print(seasons['Rainy'][1])


#Dictionary Methods
#get() is a useful method to access the
#values of a key iin a dictionary
print(capitals.get('UP'))

#Duplicates not allowed
#Dictionary cannot have two items with same keys

dict2 = { 
          "brand": "Maruti",
          "Model": "Breeza",
          "year": 2021,
          "year": 2020 
        }
print(dict2)


#Loop through Dictionary, it will show only keys
for x in dict2:
    print(x)
#print all values in the dictionary, one by one:
for x in dict2:
    print(dict2[x])
    
##############################################################