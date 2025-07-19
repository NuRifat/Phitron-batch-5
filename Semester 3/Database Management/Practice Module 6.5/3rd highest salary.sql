USE dummydb;

-- 3rd Highest salary employee

-- Naive approch, will give all the person who have less than 2nd highest salary 
SELECT *
FROM employees
WHERE salary < ( SELECT MAX(salary)
	FROM employees 
    WHERE salary < ( SELECT MAX(salary)
	FROM employees
    )
);

-- best approach, even if asking for the 10th/100th highest one
SELECT DISTINCT Salary
FROM employees
ORDER BY Salary DESC
LIMIT 1 OFFSET 2;

-- to get employees with 3rd highest 
SELECT *
FROM employees 
WHERE Salary = (
	SELECT DISTINCT Salary
	FROM employees
	ORDER BY Salary DESC
	LIMIT 1 OFFSET 2
);