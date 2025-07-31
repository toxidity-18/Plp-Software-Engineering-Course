# variable 
site_name = 'Power learn Project' # string 
number_of_modules = 6 # integer
points = 5.7  # floats
worthiness = True # boolean 
# changing the value of variables 
site_name = 'Odin Project'
# assigning multiple value to multiple variable names 
a,b,c = 1,2,'Hello am the new python programmer in town'
print(a)
print(b)
print(c)
# variable as the storage area 
number = 10


## Data types 
# variables 
name = 'Python development'
print (name)
# list 
fruits = ['apple','banana','orange']
print (fruits)
# tuple
coordinates = (10.0, 20.0)
print(coordinates)
# dictionary
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person)
# set
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
# boolean   
True
False
# set {} list and dict [] tuple ()
# Arithmetic Operators
# +, -, *, /, //, %, **
# Building blocks 
a = 5
b = 2
# bui;ding equipments 
## addition this is cement 
a+b # 7
print (a+b)
## subtraction this is chisel 
a-b # 3
print (a-b)
## division is to share equally 
a/b # 2.5
print (a/b)
## multiplication this is like adding tile to the floor / making groups 
a*b # 10
print (a*b)
## floor division used when we have leftover that is remainders 
a//b # 2
print (a//b)
## modulus this is like the remainder of the division
a%b # 1
print (a%b)
## exponentiation this is like the power of a number
a**b # 25
print (a**b)  
## NB : The main difference about floor division and modulus is that floor division ignores the remainder but modulus give the remainder but rounds it off .
# Comparison Operators
# ==, !=, >, <, >=, <=
a=5
b=3
## == is it the same 
a==b # False
## != is it not the same
a!=b # True
##> is it bigger 
a>b # True
## is it smaller 
a<b # False
## >= is it bigger or equal to
a>=b # True
## <= is it smaller or equal to
a<=b # False
## Assignment Operators 
## give a name to my toy 
my_toy = 'teddy bear'
## plain assignment 
a # name 
5 # value
a=5
## add something to my value (increment)
a+=2# a=a+2 # 7
## taking something away from my value (decrement)
a-=2 # a=a-2 # 5
## multiply my value by something (multiplication)
a*=2 # a=a*2 # 10
## divide my value by something (division)
a/=2 # a=a/2 # 5.0
## floor divide my value by something (floor division)
a//=2 # a=a//2 # 2.0
## modulus my value by something (modulus)
a%=2 # a=a%2 # 0.0
## exponent my value by something (exponentiation)
a**=2 # a=a**2 # 25.0
## Logical Operators
# and, or, not
## and both ought to be true 
is_sunny = True
is_warm = True
is_weekend = False
is_sunny and is_warm # True
is_sunny and is_weekend # False
## or either ought to be true
is_sunny or is_warm # True
is_sunny or is_weekend # True
## not negates the value
not is_sunny # False
not is_warm # False
not is_weekend # True
## practise
age = 10
age >5 and age<13 # True
age >5 or age<13 # True
not (age >5 and age<13) # False
## Membership Operators
# in, not in
fruits = ['apple', 'banana', 'orange']
'banana' in fruits # True
'grape' in fruits # False
'a' in fruits[0] # True
'grapes' not in fruits # True
## real world example 
password = 'hello123'
if '123' in password :
  print('Password is weak')
else:
  print('Password is strong')