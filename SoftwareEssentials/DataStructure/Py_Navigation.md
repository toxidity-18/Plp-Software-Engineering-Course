<!-- # Data Structure .

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
      print(coordinates[0])) -->





# 🌟 Python Basics for Beginners: Summary + Easy Guide

---

## 1. 🧱 What is Python?

> Python is a simple, powerful programming language used to build websites, apps, games, and even control robots.

It’s loved because:

* It’s **easy to read** (like English).
* You can use it to do **almost anything**.

---

## 2. 🧠 Data Types & Variables

Think of **variables** as labeled boxes that hold data. Python has different “box types” (data types).

### ✅ Examples:

```python
age = 25              # int (whole number)
height = 5.75         # float (decimal)
name = "Samuel"       # str (text)
is_student = True     # bool (True or False)
```

### 🧪 Check the type of any variable:

```python
print(type(age))  # Output: <class 'int'>
```

---

## 3. 🔀 Control Flow (Making Decisions)

Use **if, elif, else** to make your code “think” and act based on conditions.

### ✅ Example:

```python
temperature = 30

if temperature > 25:
    print("It’s a hot day! ☀️")
else:
    print("It’s a cool day! ❄️")
```

### 🎓 Student Grading Example:

```python
marks = int(input("Enter marks: "))

if marks > 70:
    print("Grade: Distinction 🏆")
elif marks >= 60:
    print("Grade: Credit 🎖️")
elif marks >= 50:
    print("Grade: Pass 👍")
else:
    print("Grade: Fail ❌")
```

---

## 4. 🔁 Loops (Doing Things Again and Again)

### ➤ `for` loop: Repeat something a set number of times.

```python
for i in range(5):
    print(i)  # Prints 0 to 4
```

### ➤ `while` loop: Repeat something while a condition is true.

```python
countdown = 3

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1

print("Blast off! 🚀")
```

---

## 5. 📚 Organizing Data: Lists, Tuples, Sets, Dictionaries

---

### ✅ Lists: A changeable collection of items

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
```

---

### ✅ Tuples: A fixed (unchangeable) collection

```python
coordinates = (10, 20)
print(coordinates[0])  # 10
```

---

### ✅ Sets: Unordered, no duplicates

```python
unique_numbers = {1, 2, 2, 3}
print(unique_numbers)  # {1, 2, 3}
```

---

### ✅ Dictionaries: Data stored as key-value pairs

```python
student = {"name": "Sam", "age": 20}
print(student["name"])  # Sam

student["age"] = 21
print(student)  # {'name': 'Sam', 'age': 21}
```

---

## 6. 🦸‍♂️ Functions (Reusable Code)

Functions let you reuse code and stay organized.

### ✅ Example:

```python
def greet(name):
    print("Hello,", name + "! 👋")

greet("Alice")
greet("Samuel")
```

### ✅ Return a value:

```python
def add(x, y):
    return x + y

print(add(3, 5))  # 8
```

---

### 💻 Mini-Challenge: Even or Odd Checker

```python
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is even ⚖️")
    else:
        print(number, "is odd 🎯")

check_even_odd(7)  # Try with any number
```

---

## 7. 🧰 Modules (Python’s Toolkit)

Modules = pre-built tools you can import and use.

### ✅ Example 1: `math` module

```python
import math
print(math.sqrt(16))  # 4.0
```

### ✅ Example 2: `random` module

```python
import random
print(random.randint(1, 6))  # Rolls a virtual die (1-6)
```

---

## 🧠 Recap: What You’ve Learned

| Topic                          | What It Does                   |
| ------------------------------ | ------------------------------ |
| **Variables & Types**          | Store info (name, age, etc.)   |
| **Control Flow**               | Make decisions (if-else)       |
| **Loops**                      | Repeat tasks (for, while)      |
| **Lists, Tuples, Sets, Dicts** | Store and organize data        |
| **Functions**                  | Reuse code blocks              |
| **Modules**                    | Use tools others already built |

---

## 📣 Final Tip:

> Don’t rush. Build slowly. Run your code. Make mistakes. Fix them. That’s how real programmers learn. 💡

Would you like a free beginner practice project next (like a number guessing game, simple calculator, or quiz app)? I can guide you step-by-step.
