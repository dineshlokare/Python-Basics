
"""Python Code To add all items in the list"""

def sum_list(items):
    sum=0
    for x in items:
        sum=sum+x
    return sum
print(sum_list([4,3,-1]))

############################################################

"""Python code to multiply all items in the list"""

def mul_list(items):
    mul=0
    for x in items:
        mul=mul*x
    return mul
print(mul_list([2,4,3]))

#################################################################

"""Python program to count the numbers of strings which stisfies
    the condition that the string length is 2 or more and the first and 
    last character from a given list of strings  given a list
    ['abc','syz','aba','1221']    """

def match_words(words):
    ctr = 0
    for word in words:
        if len(word)>2 and word[0] == word[-1]:
            ctr +=1
    return ctr
print(match_words( ['abc','syz','aba','1221']))

#####################################################################

"""
   Write python program to get a list, sorted in increasing order by the
   last element in each tuple from a given list of non-empty tuples.
   Sample List: [(2,5),(1,2),(4,4),(2,3),(2,1)]
   Expected result: [(2,1),(1,2),(2,3),(4,4),(2,5)]
"""
 
def last(n):
    return n[-1]

def sort_list_last(tuples):
    result=sorted(tuples,key=last)
    return result
print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))

######################################################################

"""Write a python program to remove duplicates from a list.
    given the list a = [10,20,30,20,10,50,60,40,80,50,40]
"""
lst1 = [10,20,30,20,10,50,60,40,80,50,40]
st1 = set(lst1)
#since set reomves duplicate items, hence list in converted to set
print(st1)
lst2=list(st1)
print(lst2)

############################################################

""" write a python program to clone or copy a list
"""
original_lst=[12,32,42,12]
new_list = list(original_lst)
print(original_lst)
print(new_list)

###########################################################

""" Write a python program to find the list of words that are long than
    n from a given list of words 
"""
def long_words(n,str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(long_words(3, "The quick brown fox jumps over the lazy dog"))

###############################################################

""" Write a python function that takes two lists and returns
     true if they have at least one common member.
"""
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x==y:
                result = True
                return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

############################################################

""" Wrtie python program to calculate the difference between two
    lists
"""

list1 = [1,3,5,7,9]
list2 = [1,2,4,6,7,8]
diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
total_diff = diff1 + diff2
print(total_diff)

##################################################################
#important question is used in NLP
""" write python program to convert list of character into a string.
"""
s = ['a','b','c','d']
str1 = ''.join(s)
print(str1)

#################################################################

"""write a python program to find the index of an item in a
    specified list.
"""
# imp question

num = [10,30,4,-6]
print(num.index(30))

####################################################################

"""write a python program to append a list to the second list"""

list1 = [1,2,3,0]
list2 = ['Red','Green','Black']
final_list = list1 + list2
print(final_list)





