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

/*  -- Transaction 
-- START transaction;
-- apply changes of transaction 
-- COMMIT ;
-- revert changes : 
-- ROLLBACK ;
-- Intsruct my SQL not to start transaction or commit change 
-- SET AUTOCOMMIT = OFF ;
CREATE DATABASE stadium;
CREATE DATABASE stadium;
USE stadium;
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255)
);
-- commit example
START TRANSACTION;

INSERT INTO users (id, username) 
VALUES (1, 'peter');

UPDATE users 
SET email = 'peter@mail.com' 
WHERE id = 1;
COMMIT;
SELECT * FROM users;
-- rollback 
START TRANSACTION;
INSERT INTO users (id, username) 
VALUES (2, 'sharon');

UPDATE users 
SET email = 'sharon@mail.com' 
WHERE id = 2;
ROLLBACK;

-- Aggregate function : 
	-- AVG : cal avg value in a set of values .
	SELECT 
		AVG(buyPrice) avg_buy_price
	FROM 
		products;
	-- Count return number of values inside a set .
    SELECT 
		COUNT(*) AS total
	FROM 
		products;
	-- Max maximum value inside a set .
    SELECT 
		MAX(buyPrice) highest_price
	FROM 
		products;
	-- Min minimum value inside a set .
    SELECT 
		MIN(buyPrice) lowest_price
	FROM 
		products;
	-- Sum return sum of values in set .
    SELECT 
		productCode, 
		SUM(priceEach * quantityOrdered) total
	FROM
		orderDetails
	GROUP BY productCode
	ORDER BY total DESC;
    -- Group by : group order statues .
    SELECT 
	  status 
	FROM 
	  orders 
	GROUP BY 
	  status;
    -- Obtain number of orders on each status 
    SELECT 
	  status, 
	  COUNT(*) 
	FROM 
	  orders 
	GROUP BY 
	  status;
	-- total amount of each order 
    SELECT 
	  orderNumber, 
	  SUM(quantityOrdered * priceEach) AS total 
	FROM 
	  orderdetails 
	GROUP BY 
	  orderNumber;
	-- Having : apply condition to the group returned by Group by and only include groups which meet specified conditions .
    SELECT 
	  ordernumber, 
	  SUM(quantityOrdered) AS itemsCount, 
	  SUM(priceeach * quantityOrdered) AS total 
	FROM 
	  orderdetails 
	GROUP BY 
	  ordernumber 
	HAVING 
	  total > 1000;
      */
      