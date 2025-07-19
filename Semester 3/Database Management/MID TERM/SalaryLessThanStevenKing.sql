USE dummydb;

SELECT * FROM employees
WHERE Salary < (SELECT Salary FROM employees
				WHERE first_name = 'Steven' AND last_name = 'King');