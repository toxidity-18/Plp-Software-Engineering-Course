-- Create a new database named 'mydb'
CREATE DATABASE mydb;

-- Switch to using 'mydb'
USE mydb;

-- Create the Employees table with the specified columns and constraints
CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,         -- Unique ID for each employee
    first_name VARCHAR(50) NOT NULL,     -- Employee's first name
    last_name VARCHAR(50) NOT NULL,      -- Employee's last name
    hourly_pay INT NOT NULL,             -- Hourly pay in whole numbers
    hire_date DATE NOT NULL               -- Date the employee was hired
);

-- Show all rows from Employees (currently empty)
SELECT * FROM Employees;

-- Insert first employee's data
INSERT INTO Employees (employee_id, first_name, last_name, hourly_pay, hire_date)
VALUES (1, 'Eugene', 'Krabs', 25, '1975-10-20');

-- Insert second employee's data
INSERT INTO Employees (employee_id, first_name, last_name, hourly_pay, hire_date)
VALUES (2, 'Spongebob', 'Squarepants', 18, '1999-10-25');

-- Insert third employee's data
INSERT INTO Employees (employee_id, first_name, last_name, hourly_pay, hire_date)
VALUES (3, 'Squidward', 'Q.Tentacles', 15, '1975-10-28');

-- Show all rows from Employees again
SELECT * FROM mydb.Employees;

-- Insert two more employees in a single statement
INSERT INTO Employees (employee_id, first_name, last_name, hourly_pay, hire_date)
VALUES
    (4, 'Sandy', 'Cheeks', 10, '1975-10-19'),
    (5, 'Plankton', 'Sheldon', 30, '1978-08-23');

-- Show all rows from Employees table
SELECT * FROM Employees;

-- Show structure/columns of Employees table
DESCRIBE Employees;
SHOW COLUMNS FROM Employees;

-- Update hire date for the employee whose ID is 2 (Spongebob)
UPDATE Employees
SET hire_date = '1975-10-21'
WHERE employee_id = 2;
