<!-- # Introduction 
-[ROADMAP](https://www.canva.com/design/DAF8G-4JKug/vIqPiE9u98khAy7yRHThkw/edit).
- Python is a high level interpreted programming language used for  many different purposes .

     1) Web development .
     2) Computing 
     3) Machine learning .
     4) Hacking 

- Many different purposes thus versatile .
- Large and active community .
- Cross-platform compatible : thus runs on many different platforms .
- Plenty of libraries .

## Python variables .
- Assignment operator to assign variables to values .
- Variable is a container which store data .

```python
        # Variable as the storage area
        number = 10

        # site_name assigned to value of 'power learn project'
        site_name = 'Power learn Project'
        print(site_name)# output : Power learn Project 
        # changing the value of variables in python 
        # change the value Power learn Project to Odin Project 
        site_name = 'Odin Project'
        print(site_name)
        # assigning multiple value to multiple variables in one line 
        a.b.c = 1,5.32,'Hello'
        print (a)
        print (b)
        print (c)
        # multiple variable to the same value 
        site_1-site_2='Power learn Project'


```
## Rules of naming variable 
- There are case sensitive and also use underscores instead of camel cases .

## Data types 
- This are the types of data which can be stored inside variables .
- They include :

  1) Numeric : i.e int,floats , complex which store numeric values 
  2) String : str which contain a series of characters .
  3) Sequence : list,tuple and range which contain a collection of character .
  4) mapping:dict which holds data in key/value pairs .
  5) Boolean : bool i.e true of false 
  6) Set : they hold a series of unique names .
- NB : Everything in python is an object . Thus the term OOP .
- Examples of this data type in code 
```python
    # numeric values 
    num_1 = 45
    num_2 = 5.67
    print(num_1) # int 
    print(num_2)# float NB: Accurate to a range of 15 decimal places 
    # string 
    name = 'Python Developer'
    print(name)
    # sequence 
     # List : ordered collection separated with commas and enclosed with square brackets 
       languages = ['Python','Javascript','2','Frontend development','Backend development']
       print(languages)
       # to access specific data inside this list will use ..
       print(language[0])
       print(language[1])
    # Tuple : same as list but they immutable thus cannot be changed once they are created they remain the same .
       religion = ('Christian','Muslim','Hindu','Buddha')
       print(religion(0))
    # Set : unordered unique collection of items 
       student<_id_based_on_performance = {112,114,118,119}
       print(student_id_based_on_performance)
    # Dict : they mainly deal with key:values pairs 
       person = ['name':'Sam','age'=19]
       print(person)

```
## Basic operations 
- Type of python operation :
 
 1) Arithmetic operator 
 2) Assignment operators
 3) Comparison operators .
 4) Bitwise operators .
 5) Logical operators .
 6) Specials operators .

 - Arithmetic operators 
    1) They are used to do mathematical operation on python : addition , subtraction , division , multiplication , exponentiation (power), floor division , float division ,modular(remainder).
    ```python
    add = 2+5
    sub = 4-3
    times = 2*3
    exp= 4**2
     -->

# Operation in python
## Arithmetic Operators 
- Think of number as building block and our operators as building equipments .
```python
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
```
## Comparison operators 
- Basically a matter of finding out if it true or false .
```python
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
```
## Assignment Operators 
- This is like giving name to thing or giving value or adding data .
```python
   