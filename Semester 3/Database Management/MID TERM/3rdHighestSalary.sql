USE dummydb;

-- 3rd highest salary
SELECT MAX(Salary) FROM employees
WHERE Salary < (SELECT MAX(Salary)
				FROM employees
                WHERE Salary < (SELECT MAX(Salary)
								FROM employees
                                )
				);