USE dummydb;

-- Show the list of employee name and corresponding manager names. (self JOIN)
SELECT e.first_name AS Employee_name, m.first_name AS Manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
