# Python : Built in Data Structure .

## What are data structures .
1)  Variable can store : integers , booleans or strings .
2) When handling complex data we use data structures , (why) Help organize and arrange data so that operation can be performed on them .
3) Type of data structure :

  -  Built in data structure : list , tuple , dictionary & set .
  - User defined data structure : stack , tree , queue, linked list , graph & hash map .

4) Common feature about : Built in data structure is that they are non-primitive (classed as objects) .
5) D_S can be used to solve particular problems or perfect existing solutions .

###  Mutability and immutability .
1) D_S can either be mutable or immutable .

  - Mutable : changed or modified : updated , deleted eg : list .
  - Immutable : unchanged or they don't allow any modification once the data is set .

## List and tuples .
1) List can be used to store multiple data at once eg : shopping list .

### Creating a list .
1) List can store items of different data type and also the same data types .
```python
  list_a = [1,2,3,4,5] # int
  list_b = ['sam','kam'] # strings 
  list_c = ['sam',2,4.5] # str and int 
  list_d = [True] # bool
  list_e = [1,2,['sam',False],4.5] # nested list
  ```
### Accessing item on a list .
1) Through use of index i.e : 0,1,2,3,4 etc .
```python
list_a [3] # 4
list_b [0] # 'sam'
```
### Slicing python list .
1) It possible to access items on a list through slicing operators i.e : : , -ve int 
```python
  list_f = [1,'sam',3.5,'kam',[1,True],False]
  list_f[0] # 1
  list_f[2:5] # 3.5, 'kam',[1,True]
  list_f[-3] # 'kam'
  list_f[2:] # 3.5,'kam',[1,True],False
```
### Adding elements on a list .
1) How to add items on a list :

  - Using the append() method which add item at the end of the list .
  ```python
  numbers = [1,2,3,4]
  numbers.append(5) # [1,2,3,4,5]
 ```
 - Using extend() which adds all items on a list to another list .
 ```python
  prime_num=[2,3,5]
  even_num=[0,2,4,6]
  even_num.extend(prime_num) # [0,2,4,6,2,3,5]
```
### Changing element inside a list
1) To change the elements inside a list we will use to = operator .
### Removing items on a list .
1) In python we can use the following to remove items in a list :

  - Using the del statements : Check the Wk2.py file for the relevant codes .
  - Using the remove function  : '' 
  - NB : The remove function only take one argument .
  - NB : When you want to remove more than one argument be sure to use the del statement with the relevant index
### Python list methods .
1)  Type of python list methods and what they do :

  -  Insert add an item at a specific position without replacing the original one .: Check code 39 to 40 .
  - .pop remove item on a list through use of index .
  - NB : .remove uses the value itself .
  - .reverse , 1 to 5 changes to be 5 to 1 .
  - NB : reverse takes in no values .
  - .count , count how many items are on a list .
  - .sort , arranges the list in ascending to descending order .
  - .clear , this is the ultimate delete feature .Removes all the items on a list .
### Iterating through a list .
1) Using loops to iterate over elements inside a list .

   - Print out the element separately as it loops over them thus assigning them to the given variable .

### List comprehension .
1) This is another form of creating list through use of expressions and for statement inside [].

## Tuples .
1) Tuples are similar to a list the difference is that we cannot change the elements inside a tuple .
2) Created with use of parantheses .
3) Type function allows us to know which class variable a function belongs too .
 4) Code ln 65 to 69 are different because of the closing comma in between them .
### Accessing tuple 
1) Like list each tuple has a specific index value .

  - Indexing : Using the indexing operator , 
  - NB : Index error this occurs when you try to access an item outside the range of indices .
  - NB : TYpe error the indexes must be an int and  not a float or any other data type .
  - Negative indexing : -1 represent the last item on my tuple so on so forth 
### Tuple methods .
1) Method which add or remove i.e , remove() , insert(),extend(),.pop() etc don't exist because tuple are immutable .
2) But .count() and .index() work well .
3) NB count check how many time that value is on repeat .well index check them number of index of the specific value .

## Dictionaries .
1) These are order collection which store data in key: value pairs .
2) The key is the unique id well as the value is the data passed and associated with that unique id .
### Creating A dict in python .
3) We will use {key:value } .
4) Adding element inside a dictionary we use [] .
### Changing values inside a dictionary .
5) Del statement , and also the [] .
6) Del can also delete the whole dict .
7) Member test through using in which only affect the key and not the value .

## Set 
1) This is a collection on unique data .
