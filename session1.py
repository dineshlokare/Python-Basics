
#string concatnation
age = input('print age:')
print(type(age))
print(age)

age1 = input('Please enter your age:')
print(type(age1))
print(age1)

age2 = input('Please enter your age:')
print(type(age2))
print(age2)
age=age1+age2
print(age)

#floating numbers
#Real number, or floating point numbers,
#are represented in python using the IEEE 754
#double-precision binary floating-point number format

exchange_rate = 1.23
print(exchange_rate)
print(type(exchange_rate))
###################################

#converting to floats
#As with integers it is possible to convert other
#types such as an int or a string into a float.

int_value = 100
string_value ='1.3' #string values written in single quote or double quote
float_value = float(int_value)
print('int value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('String value as a float:', float_value)
print(type(float_value))

#complex numbers

c1 = 1
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean Values
#Python supports anothe type called Boolean;
# a Boolean type can only be one of True or False

all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))
##############################
#you can also convert strings into booleans as long as the
#Ture or False(or nothing else).

status = bool(input('OK it is confirmed?:'))
print(status)
print(type(status))
############################

#Arithmetatic  operators

# in interview question will be asked

home = 10
away = 15
print(home + away)
print(type(home + away))
print(10*4)
print(type(10*4))
goals_for=10
goals_against=7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

############################################

print(100/20)
print(type(100/20))

#to ignore the fractional part the
#there is an alternative version of the divide operator
# //.
#This operator is referred to as the integer division operator 

print(100 // 20)
print(type (100 // 20))

#modulus > remainder

print('Modulus division 100 % 13 :', 100 % 13)
print( 'Modulus division 3 % 2 : ', 3 % 2)

#Power operator
a=5
b=3
print(a ** b)

#Assignment Operators

x = 0
# += is also called compound operator

x +=1 # has the same behaviour as x = x + 1

#None value
#python has a special type,
#the NoneType, with a single value, None.

winner = None
print(winner is None)
#Alternatively you can also write:
print(winner is not None)

winner = None
print('winner:', winner)
print('winner is None', winner is None)
print('winner is not None', winner is not None)
print(type(winner))
print('Set winner to True')
winner = True

########################################

#Flow of Control Using If Statements
#indentated

num = int(input('Enter a number:'))
if num > 0:
   print(num)

#Else in an If statement

num = int(input('Enter yet another number:'))
if num < 0:
    print('Its negative')
else:
    print('Its not negative')
    


