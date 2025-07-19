USE dummydb;

SELECT *
FROM employees
WHERE hire_date > (
	SELECT hire_date
    FROM employees
    WHERE first_name = 'Steven' LIMIT 1
);

-- WHAT IF TEHRE IS NO STEVEN
SELECT *
FROM employees
WHERE hire_date > COALESCE((
	SELECT MAX(hire_date)
	FROM employees
	WHERE first_name = 'Steven'
), '1900-01-01');  -- fallback date

