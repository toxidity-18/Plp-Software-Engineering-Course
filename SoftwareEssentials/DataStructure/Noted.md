# Data Structure .

## Welcome to python programming
- Python is easy and super powerful tool
- Use case :
  
  1) create website 
  2) application 
  3) crunch data 
  4) make robots smart 

## Python building blocks
- Mainly compromise of data types  and variables .
- Eg :

  1) int : whole number i.e 1,2 
  2) floats : decimal number i.e 3.14
  3) str: text i.e 'Hello , world'
  4) booleans : true or false 

- Variables : container which hold data 
```python
        age = 19
        height = 5.6
        name = 'Tracy'
        is_Student = True 
        # printing it out 
        print (name)
        print (height)
        print (age)
        print (is_Student)
```
- Using type function to check a variables data type :
``` python
         # type function 
         type(age)
         type(name)
         type(height)
         type(is_Student)
```

## Control flow 
- Python can make decision based on certain conditions , this is done when one implements if-else statements 
```python
# remember that indentation matters a lot and also also : 
          temperature = 30
          if temperature > 25 :
              print ('It\'s a hot day')
          else :
              print ('It\'s a cold day')
```
## Adding elif for multiple condition 
- elif means else if .
```python
           #control flow for grading student performance 
           #this will ask for user inputs and grade student's performance 
           # prompt the user for user inputs 
           marks = int(input('Enter student\'s marks:''))
           # grading system through control flow
           if marks > 70:
               print('Top Credits')
           elif marks > 60:
                print('Normal Credits')
            elif marks > 50:
                print('Pass')
             else :
                print ('fail')
```
## Loop ( like pressing the repeat button)
- Repeating the same code without having to write again .
- For loop 

   1) Repeating based on a fixed number of times thus the term range .
   ```python 
             # print number between 0 - 4
             for i in range(5):
                  print(i)
    ```
- While loop
   
    1) Runs as long as the condition is true 
    ```python
           countdown = 5
           while countdown>0:
                  print ('Countdown:', countdown)
                  countdown -=1
    ```

## List sets tuples and dictionaries
- Ways in which python organizes it's data .
1) List 
   
   - Ordered collection of data which is mutable means can change , it's great for storing multiple items 
  - List of shopping list .
  ``` python 
  fruits = ['Apples', 'Bananas', 'Cherry']
  # accessing this elements or data 
  print(fruits[0]) # Apple
  # changing mutability 
  fruit[1] = Orange 
  fruit[0]= watermelon 
  print(fruit)
  ```
2) Tuples 

  - Ordered collection which is immutables thus cannot change like list .
  ```python
      coordinates = (10,20)
      print(coordinates[0]))