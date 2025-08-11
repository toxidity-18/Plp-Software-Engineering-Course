# Data 
- Meaning of data : collection of information which is processed , organized and analyzed 
# Information 
- This is data which can be processed , organized and analyzed .
# Type of Data 
1) Structured data :
- Think of a bookshelf : highly organized and follows strict format .
2) Semi-structured 
- Not very organized : think of a messy school desk .
3) Unstructured
- Free not really organized .

# Database 
- Structured collection of data which can be managed processed and updated .
- Eg : School inside that school we have teacher , students and classes .
      
      1) school is a container that hold many tables of data : database 
      2) student,teacher and classes structure set of data : table via row and columns .
      3) row is one record of data : one student , one teacher or one class .
      4) column is one field : age , name or email 
      5) field is the actual data : name = Tracy Reene .
# Terms and terminologies
## Data types 
- Ensures that all information goes in the right places that is num for counting text for names .
## Primary key 
- Unique identifier for each row thus might acts as a vip pass
- Eg: Admission number for students , name of class 
- Must be unique and cannot be NULL , One primary key per table
```SQL
   CREATE TABLE students (
  student_id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT
);
```
## Foreign key 
- Connect one table to the other i.e student table to class table where some student are in a specific or the same class .
```SQL
  CREATE TABLE classes (
    class_id INT PRIMARY KEY,
    class_name VARCHAR(50)
  );

  CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
  );
```
## Auto Increment 
- Automatically increase the number of row when a new table is added 
```SQL
  CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100)
);
```
## NOT NULL
- Simply that value should not be null , cannot be empty .
```SQL
  name VARCHAR(100) NOT NULL
```
## Unique 
- Make sure no set of rows have the same name 
```SQL
  email VARCHAR(100) UNIQUE 
```
## Check
- Check that a condition of rules have been meant.
```SQL
  age INT CHECK (age>=18)
```
## Default 
- Give columns default value when it empty 
```SQL
  status VARCHAR(10) DEFAULT 'active'
```
## Index 
- Makes searching faster
```SQL
  CREATE INDEX idx_name ON students(name);
```

```SQL
  -- Create a new database named 'school'
  CREATE DATABASE school;

  -- Switch to the 'school' database so we can create tables inside it
  USE school;

  -- Create a table to store all class details
  CREATE TABLE classes (
    -- 'class_id' will be a unique number for each class
    -- AUTO_INCREMENT means it increases automatically for each new class
    -- PRIMARY KEY means this is the unique identifier for each row
    class_id INT AUTO_INCREMENT PRIMARY KEY,

    -- 'class_name' is the name of the class (e.g., "Math", "English")
    -- VARCHAR(50) means it stores text up to 50 characters max
    -- NOT NULL means it must always have a value (can't be empty)
    class_name VARCHAR(50) NOT NULL
  );

-- Create a table to store student details
CREATE TABLE students (
  -- Unique student ID that auto-increments each time a student is added
  student_id INT AUTO_INCREMENT PRIMARY KEY,

  -- Student's name: up to 100 characters, and cannot be left empty
  name VARCHAR(100) NOT NULL,

  -- Student's age: must be greater than 10
  age INT CHECK (age > 10),

  -- This is a foreign key: it links to 'class_id' in the 'classes' table
  -- It means each student is enrolled in a class
  class_id INT,

  -- Define the foreign key relationship
  FOREIGN KEY (class_id) REFERENCES classes(class_id)
);
```
## Type of data models 
- They describe how we connect and organize data .
- They include :
  
  1) Hierarchical model : they organize data in a tree like structure thus one parent per child eg file directory or parent to child .
  2) Network models : they are more flexible thus each model can have multiple connections eg telecommunications .
  3) Relational models : store data in tables which can be linked via relationships eg student relation to class and teachers 
  4) Object oriented models : store data as tables which is useful for complex structure eg game characters or video games .

# Introduction to SQL 
- Long form is structured query language .
- Basically it helps processes , store , manages, update data .
- Creating a data you 
   
  1) draw rough design of that data : what it about and what is does or needed to be done etc 
  2) identify the key data points : value name time etc 
  3) data types : names given to this data point .
  

  ___
  
 