USE rifatlearningdb;

-- List of all employees with their department names
SELECT e.name, e.position, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- Find average salary by department:
SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;

-- List all department heads with department name:
SELECT d.department_name, e.name AS department_head_name
FROM departments d
JOIN employees e ON d.department_head_id = e.employee_id;

-- Find the highest paid employee in each department:
SELECT d.department_name, e.name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE (e.salary, e.department_id) IN (
	SELECT MAX(salary), department_id FROM employees GROUP BY department_id
);