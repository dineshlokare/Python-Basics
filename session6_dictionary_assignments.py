"""
    Write a python scipt to add a key to a dictionary
    #Sample Dictionary: (0:10, 1:20)
    #Expected Result: (0:10, 1:20, 2:30)
"""
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)
#two ways
d = {0:10, 1:20}
print(d)
d[2]=30
print(d)

###########################################################

"""
    write a python script to concatenate the following dictionaries to create
    a new one
    Sample Dictionary :
        dic1={1:10, 2:20}
        dic2={3:30, 4:40}
        dic3={5:50, 6:60}
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic4={}
for d in (dic1, dic2, dic3) : dic4.update(d)
print(dic4)

############################################################

"""
    Write a python script to check given key already exist in dictionary
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print("key is present in the dictionary")
    else:
        print("key is not present in the dictionary")
is_key_present(5)
is_key_present(7)

#################################################################

"""Write a python program to iterate over dictionaries using for loops"""

d = {'x':10, 'y':20, 'z':30}
for dic_key, dic_value in d.items():
    print(dic_key,':',dic_value)










