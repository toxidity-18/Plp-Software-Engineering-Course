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

-- insert data into the teachers table 
INSERT INTO teachers (name, email, phone, address, date_of_birth)
VALUES
('Alice', 'alice.kimani@example.com', '+254723478', 'Nairobi', '1995-08-10');

INSERT INTO teachers (name, email, phone, address, date_of_birth)
VALUES
('Brian', 'brian.otieno@example.com', '+2548765432', 'Kisumu', '1990-02-25');

INSERT INTO teachers (name, email, phone, address, date_of_birth)
VALUES
('Carol', 'carol.wanjiku@example.com', '+25434567', 'Mombasa', '1988-12-15');
