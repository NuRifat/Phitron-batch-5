USE dummydb;

WITH avg_salary AS (
	SELECT AVG(Salary) AS sal
    FROM employees
    )
SELECT * FROM employees
WHERE Salary > (SELECT sal FROM avg_salary);