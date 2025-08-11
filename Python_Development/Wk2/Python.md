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

