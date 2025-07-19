USE dummydb;

-- CTE using for finding 3rd highest
WITH first_max AS (
	SELECT MAX(salary) AS max1 FROM employees
),
second_max AS (
	SELECT MAX(salary) AS max2 FROM employees
    WHERE salary < (SELECT max1 FROM first_max)
),
third_max AS (
	SELECT MAX(salary) AS max3 FROM employees
    WHERE salary < (SELECT max2 FROM second_max)
)
SELECT *
FROM employees 
WHERE salary = (SELECT max3 FROM third_max);

-- CTE using for finding 3rd lowest
WITH first_min AS (
	SELECT MIN(salary) AS min1 FROM employees
),
second_min AS (
	SELECT MIN(salary) AS min2 FROM employees
    WHERE salary > (SELECT min1 FROM first_min)
),
third_min AS (
	SELECT MIN(salary) AS min3 FROM employees
    WHERE salary > (SELECT min2 FROM second_min)
)
SELECT *
FROM employees 
WHERE salary = (SELECT min3 FROM third_min);