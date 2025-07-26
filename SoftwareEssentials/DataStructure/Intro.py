# Writing variables 
age = 19
height = 5.6
name = 'Tracy'
is_Student = True 
 # printing it out 
print (name)
print (height)
print (age)
print (is_Student)
# output will be the data stored .
# using type function to check a variables data type :
type(age)
type(name)
type(height)
type(is_Student)

# practising control flow 
if age > 20 :
   print('she\'s an adult')
else:
   print('she\'s a teenager')

# Grading systems for students performances
# asking for students marks
marks = int(input('Enter your marks: '))
# checking the marks and printing the grade
if marks >= 90:
    print('Grade A')
elif marks >= 80:   
    print('Grade B')  
elif marks >= 70:
    print('Grade C')
elif marks >= 60:
    print('Grade D')
elif marks >= 50:
    print('Grade E')
else:
    print('Grade F')

# practising loops 
## for loops 
# range of number btw 0 -4
for i in range (5):
    print(i)
## while loops 
countdown = 5
while countdown > 0 :
    print(countdown)
    countdown -= 1  # decrementing the countdown  

## collection of data in python 
# list 
fruits = ['apple', 'banana', 'cherry']
# printing the list
print(fruits)
# accessing elements in the list
print(fruits[0])  # first element
print(fruits[1])  # second element
print(fruits[2])  # third element
# adding an element to the list
fruits.append('orange')
# printing the updated list
print(fruits)
# removing an element from the list
fruits.remove('banana')
# printing the updated list after removal
print(fruits)   
#TUPLES
# tuples are immutable lists
fruits_tuple = ('apple', 'banana', 'cherry')
# printing the tuple
print(fruits_tuple)
# accessing elements in the tuple
print(fruits_tuple[0])  # first element
print(fruits_tuple[1])  # second element
print(fruits_tuple[2])  # third element
# trying to add an element to the tuple (will raise an error)
# fruits_tuple.append('orange')  # this will not work since tuples are immutable
# trying to remove an element from the tuple (will raise an error)
# fruits_tuple.remove('banana')  # this will not work since tuples are immutable      
# DICTIONARIES
