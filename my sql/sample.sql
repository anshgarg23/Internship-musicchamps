CREATE DATABASE CompanyDB;
USE CompanyDB;
CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);
INSERT INTO Employee VALUES (1, 'Alice', 30, 'HR', 50000.00);
INSERT INTO Employee VALUES (2, 'Bob', 28, 'IT', 60000.00);
INSERT INTO Employee VALUES (3, 'Charlie', 35, 'Sales', 55000.00);
INSERT INTO Employee VALUES (4, 'Diana', 26, 'IT', 62000.00);
INSERT INTO Employee VALUES (5, 'Ethan', 40, 'Finance', 70000.00);
SELECT * FROM Employee;
SELECT name, department FROM Employee;
SELECT * FROM Employee ORDER BY salary DESC; #sorting and filtering 
DELETE FROM Employee WHERE id = 3; #deleting 
UPDATE Employee
SET department = 'HR'
WHERE id = 4; # updating
SELECT * FROM Employee
ORDER BY department;
