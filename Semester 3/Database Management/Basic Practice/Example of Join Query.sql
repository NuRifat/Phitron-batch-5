USE dummydb;

-- select department which dont have any employee
SELECT d.department_name
FROM departments d LEFT JOIN employees e
ON d.department_id = e.department_id
WHERE e.department_id IS NULL;

-- select department name which minimum salary is greater than 5000
SELECT department_name
FROM departments d 
JOIN employees e
	ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING MIN(e.salary) > 5000;