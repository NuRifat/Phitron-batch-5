USE dummydb;

-- Show the employee names and corresponding job_titles without using JOIN query
SELECT e.first_name, j.job_title
FROM employees e, jobs j
WHERE e.job_id = j.job_id;

-- Using JOIN query
SELECT e.first_name, j.job_title
FROM employees e
JOIN jobs j 
ON e.job_id = j.job_id;