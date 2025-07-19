USE dummydb;

-- 3rd lowest salary
SELECT *
FROM employees
WHERE salary = (
	SELECT DISTINCT salary
    FROM employees
    ORDER BY salary ASC
    LIMIT 1 OFFSET 2
);