"""------------------------File Handling----------------------------"""

# the open() fucntion needs
#one argument: the name of the file you want to open.
#loading file to primary memory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
#Observe the extra line at the end of output

###########################################################

#To avoid this rstrip() method is used
with open('pi_digits.txt') as file_object:
    # the open() fucntion needs
    #one argument: the name of the file you want to open.
    contents = file_object.read()
print(contents.rstrip())

#rstrip() methon removes, or strips, any whitespace
#character from the right side of a string

#################################################################

"""
    Two types of path: relative path and absolute path
    #Relative paths-> only file name, for eg:- pi_digits.txt
    #Absolute paths-> w.r.t to windows :- c:\windows\system\file_name.txt
    #windows support back slash '\'
    #In virtual environment we use back slash '\'
    #linux support front slash '/'
    #In python we use path with front slash '/'
"""

file_path = 'c:/1- Python/pi_digits.txt'
with open(file_path) as file_object:  #file_object instance of file
    contents = file_object.read()
print(contents.rstrip())

######################################################################
#Reading line by line 

file_name = 'pi_digits.txt'
#we assign the name of the file we're reading from to the variable
with open (file_name) as file_object:
    #we again use the with syntax to
    #let python open and close
    #the file properly.
    
    for line in file_object:
        print(line.rstrip())
        
######################################################################

#working with a File's contents
#After you've read file into memory,
#you can do whatever you want with that data

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        print(pi_string)
        print(len(pi_string))
##################################################################

#writing to a file
# One fo the simplest ways to save data is to write it
# to a file. When you write text to a file,
# the output will still be available after
#  you close the terminal containing you program's count

file = 'programming.txt'

with open(file,'w') as file_object:
    file_object.write('I do datascience.')

###################################################
#writing multiple lines
# The write() function doesn't add any newlines
# to the text you write. so if
# you write more than onne line without 
# including newline characters
#Write() removes previous data and writes new one

filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write('I Am software engineer\n')
    file_object.write('I develop a software \n')

################################################################
#append the file 
#whe you open a file in append mode,
#pyrthon returning the file object.
#adds data in the existing present data in file

filename = 'programming.txt' 
with open(filename, 'a') as file_object:
    #we use the 'a' argument to open the file for appending
    #rather than writing over the existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

#read file
filename='programming.txt'
with open(filename) as file_object:
    f = file_object.read()
print(f.rstrip())
