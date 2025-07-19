USE dummydb;

SELECT departments.department_name, count(*)
FROM employees JOIN departments
USING (department_id) 
GROUP BY department_id;