# Creating a list .
list_a = [1,2,3,4,5] # int
list_b = ['sam','kam'] # strings 
list_c = ['sam',2,4.5] # str and int 
list_d = [True] # bool
list_e = [1,2,['sam',False],3.4] # nested list 
# Accessing elements in a list .
list_a[0] # 1
list_b[1] # 'kam'
list_c[2] # 4.5
list_d[0] # True
list_e[2][0] # 'sam'
# Slicing elements in a list .
list_f = [1,'sam',3.5,'kam',[1,True],False]
list_f[0] # 1
list_f[2:5] # 3.5, 'kam',[1,True]
list_f[-3] # 'kam'
list_f[2:] # 3.5,'kam',[1,True],False
# Adding elements in a list .
# append()
numbers = [1,2,3,4]
numbers.append(5) # [1,2,3,4,5]
#extend()
prime_num=[2,3,5]
even_num=[0,2,4,6]
even_num.extend(prime_num) # [0,2,4,6,2,3,5]
# changing the element inside a list .
list_b.append('Gich')
list_b[2] = 'Dev'# this will change Gich to Dev
# Removing elements in a list 
# Using the del statements
programming_languages = ['Python','Java','Ruby','C++','JavaScript']
del programming_languages[2] # this will remove Ruby
del programming_languages[1:2] # this will remove java c++
# Using the remove function 
programming_languages_1 = ['Java','Ruby','C++','Javascript','Python']
programming_languages_1.remove('Ruby')
# Python list methods :
language=['Python','Javascript','C++','Java']
language.insert(1,'Ruby')
print(language)
language.pop(1)
print(language)
language.remove('C++')
print(language)
language.reverse()
print(language)
language.count(1)
print(language)
language.sort() #ascending order by default .
print(language)
language.sort(reverse=True) # descending order .
# Iterating over elements inside a list .
languages=['Python','Javascript','C++','Java']
for language in languages :
  print(language)
basket = ['Apple','Mango','Pineapple']
for fruit in basket:
  print(fruit)
# List comprehension 
num = [num*num for num in range(1,10)]
print(num)
# Tuples
var_1=('Hello')
type(var_1) # this returns str .
var_2=('Hello',)
type(var_2) # this returns tuple
var_3 = 'Hello' ,
type(var_3)
# Accessing tuples 
# Indexing .
letters = ('a','b','c','d')
letters[0] # returns the value of a .
letters[-1] # return the value of d .
letters.count('c')
print(letters)
# Dictionary .
personal_details= {
'kenya':'Nairobi',
'Name':'Samuel Kamawira',
'Occupation':'Software Developer'
}
print (personal_details)
# Adding element inside a python dictionary .
personal_details['Age'] = 20
print(personal_details)
# changing element inside a dictionary .
student_id = {6384:'Samuel',1398:'Kamawira'}
del student_id[1398]
print(student_id)
student_id[1398] = 'Kamawira'
print(student_id)
student_id[1398] = 'Gichohi'
print(student_id)