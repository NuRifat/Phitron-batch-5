USE dummydb;

-- employee who got max salary
SELECT e.first_name, j.job_title, e.salary
FROM employees e
JOIN jobs j 
ON e.job_id = j.job_id
WHERE e.salary = (
	SELECT MAX(e.salary) FROM employees
);