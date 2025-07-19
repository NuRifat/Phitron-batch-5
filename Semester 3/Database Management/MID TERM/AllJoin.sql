USE dummydb;

-- INNER JOIN
SELECT employees.first_name, departments.department_name
FROM employees INNER JOIN departments
USING (department_id);

-- LEFT JOIN 
SELECT employees.first_name, departments.department_name
FROM employees LEFT JOIN departments
USING (department_id);

-- RIGHT JOIN 
SELECT employees.first_name, departments.department_name
FROM employees RIGHT JOIN departments
USING (department_id);

-- CROSS JOIN 
SELECT employees.first_name, departments.department_name
FROM employees CROSS JOIN departments
USING (department_id);