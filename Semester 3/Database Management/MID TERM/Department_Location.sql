USE dummydb;

SELECT DISTINCT departments.department_name, city
FROM departments JOIN locations
ON departments.location_id = locations.location_id;