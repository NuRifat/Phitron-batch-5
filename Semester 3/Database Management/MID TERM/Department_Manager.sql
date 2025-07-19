USE dummydb;

SELECT DISTINCT departments.department_name, employees.first_name AS Manager_name
FROM departments JOIN employees
ON departments.manager_id = employees.employee_id;
