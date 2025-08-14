# SELECT STATEMENT 

- Select help access valuable insights from your database .
- ```sql
    SELECT  (column1 , column2) ...
    FROM database . (table_name) ...
    <!-- # column and table.name fit with logic data . --> 
    <!-- SELECT * means selcet everything inside it  -->
    ```
- SELECT initiates the SQL command for retrieving data .
- PEMDAS Just like BODMAS 
- Parentheses , Exponent , Multiplication , Addition , Subtraction . (PEDMAS )
- DISTINCT This help classify unique values eg : if 50 student , half male half female ,  thus it will be .
- ```sql
    SELECT DISTINCT gender 
    FROM school.four_satima 
    <!-- output will be male and female ...  -->
    ```
- Looks at column which is being compared then output the only unique value .

## Data retrieval 
- Select * from . . . where ... like '%'
- % and _ wildcards letters .

## WILD CARD CHARACTERS 
- % and _
- _ : random characters 
- %: any amount of character 

___

1) This is the primary tool is used to interact with ones database thus retrieving the data you need .
```sql
    CREATE DATABASE school; # command for creating school database 
    USE school; # command for selecting school database 
    CREATE TABLE lessons (
        id INT AUTO_INCREMENT PRIMARY KEY ,
        title VARCHAR(100) NOT NULL ,
        name VARCHAR(20)NOT NULL,
        start_date DATE ,
        due_date DATE 
    );  # command for creating lessons tables and the required columns .
    CREATE TABLE students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) NOT NULL ,
        age INT ,
        email VARCHAR(10) NOT NULL ,
        class_name VARCHAR(10) NOT NULL
    ); # command for creating students tables and the required columns .
    INSERT INTO lessons ( title ,name , start_date ,due_date)
    VALUE ('Software engineering','Database Design','2025-08-12','2025-11-12');
    INSERT INTO lessons (title , name , start_date , due_date )
    VALUE ('Software engineering','Python programming','2025-08-12','2025-11-12');
    INSERT INTO students (name,age,email,class_name)
    VALUE('Samuel Kamawira',19,'d@gm.com','Cohort 4');
    INSERT INTO students (name,age,email,class_name)
    VALUE ('Tracy Renee',20,'t@gm.com','Cohort 4'); # command for inserting data (row) inside the created columns.
    DESCRIBE lessons; # checking the relevant tables and columns +rows created .
    DROP TABLES teachers; # deleting a table 
    CREATE TABLE teachers(
        teachers_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        phone VARCHAR(20),
        address TEXT,
        date_of_birth DATE,
        signup_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    INSERT INTO teachers (name, email, phone, address, date_of_birth)
    VALUES
    ('Alice', 'alice.kimani@example.com', '+254723478', 'Nairobi', '1995-08-10');

    INSERT INTO teachers (name, email, phone, address, date_of_birth)
    VALUES
    ('Brian', 'brian.otieno@example.com', '+2548765432', 'Kisumu', '1990-02-25');

    INSERT INTO teachers (name, email, phone, address, date_of_birth)
    VALUES
    ('Carol', 'carol.wanjiku@example.com', '+25434567', 'Mombasa', '1988-12-15');
    -- Alter the teachers table 
-- adding a new column 
    ALTER TABLE teachers 
    ADD COLUMN lesson VARCHAR(100) ;
    ALTER TABLE teachers 
    DROP COLUMN lesson ;
    -- Modify data type in specific columns 
    ALTER TABLE student 
    MODIFY COLUMN email VARCHAR(100) NOT NULL ;
    -- Renaming column name 
    ALTER TABLE lessons 
    CHANGE COLUMN due_date end_date DATE ;
    -- Adding and drop constraint .
    ALTER TABLE teachers 
    ADD CONSTRAINT chk_dob CHECK (date_of_birth < '2004-09-10')
    -- Dropping constraint 
    ALTER TABLE teachers
    DROP CONSTRAINT chk_dob ;
    -- Renaming table names 
    RENAME TABLE duration TO Time_Taken ;
    -- Truncate delete data inside tables 
    TRUNCATE TABLE students ;



```
- CREATE (DATABASE , TABLE) this create the database or the table .
- NB: id,name,varchar,int,auto_increment, etc this are keyword used when creating column field and data for rows .
- ALTER help to change or modify Table columns through modifying , adding , dropping , renaming columns , adding and drop constraint ... 
- CONSTRAINT : Rules in sql attached tables or columns thus controlling the kind of data that goes inside it .

### Wild character :
1) They are used to substitute one or more character in a string .
2) The LIKE operator are used in WHERE clause which search for specified pattern in a column .
3) WHERE select specified row in specified columns .

4) Types of operators :

    - Comparison operator :    WHERE first_name = 'Sam'
    - WHERE salary > 50000 : NB < , > , < = , > =
    - WHERE gender != Female 
    

    
