""" 
    The error signifies a situation that mostly happens dut to the
    absence fo system resources. The expceptions are the issues that can
    appear at the runtime and compile time.
    It majorly arises in the code or progrom authored by the developers.
"""
#Exceptions are handled with try-except blocks
#Handling the ZeroDivisionError Exception
print(5/0)

a=5
b=6
c=a+b
#print(5/0)
#Using try-except blocks

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
print(c)

#Using Excepitons to prevent crashes

###########################################################
"""
    Need for Encoding:- Today's programs need to be able to handle a wide 
    variety of characters. Applications are often internationalized to
    display messages and output in a variety of user-selectable languages;the
    same program might need to ouput an error message in English, Fresh, 
    Japanese, Hebrew, or Russian. Web content can be written in any of these
    languages and can also include a variety of emoji symbols.Python's string
    type uses the unicode Standard for representing characters, which lets
    python programs work with all these different possble characters.
    
    various encoding techniques that is UTF-8 Unicode transformation format
    is used as standard
    UTF-16
    UTF-32
    it can handle any unicode code point.
"""
#FileNotFoundError

filename = 'alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist!")

################################################################

