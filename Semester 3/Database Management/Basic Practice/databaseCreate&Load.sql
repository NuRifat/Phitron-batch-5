USE rifatLearningDB;

CREATE TABLE departments (
	department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    location VARCHAR(50),
    department_head_id INT
);

CREATE TABLE employees (
	employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(50) NOT NULL,
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- changing a column name
ALTER TABLE employees 
CHANGE employee_name name VARCHAR(50) NOT NULL;


INSERT INTO departments (department_name, location)
VALUES ('HR', 'Dhaka'),
('Finance', 'Chittagong'),
('IT', 'Sylhet'),
('Sales', 'Khulna');

-- Insert department heads
INSERT INTO employees (name, position, salary, hire_date, department_id)
VALUES
('Ayesha Rahman', 'HR Manager', 65000, '2020-01-15', 1),
('Karim Hossain', 'Finance Manager', 70000, '2019-11-20', 2),
('Nadia Islam', 'IT Manager', 75000, '2021-03-10', 3),
('Shuvo Ahmed', 'Sales Manager', 68000, '2018-09-05', 4);

-- Insert rest of the employees
INSERT INTO employees (name, position, salary, hire_date, department_id)
VALUES
('Samiul Haque', 'HR Assistant', 35000, '2021-06-01', 1),
('Tahmina Akter', 'HR Officer', 42000, '2022-01-10', 1),
('Hasan Mahmud', 'Accountant', 40000, '2021-07-20', 2),
('Salma Khatun', 'Finance Officer', 45000, '2022-08-01', 2),
('Tanvir Alam', 'Software Engineer', 50000, '2020-11-15', 3),
('Lamia Zaman', 'System Admin', 52000, '2021-12-05', 3),
('Imran Kabir', 'Web Developer', 48000, '2022-02-10', 3),
('Moushumi Rani', 'Sales Executive', 38000, '2021-03-18', 4),
('Jamal Uddin', 'Sales Representative', 35000, '2022-04-25', 4),
('Farhana Yasmin', 'IT Support', 40000, '2023-01-15', 3),
('Rafiul Islam', 'HR Intern', 20000, '2023-03-10', 1),
('Nilufa Sultana', 'Finance Analyst', 46000, '2023-05-01', 2),
('Zayed Khan', 'Sales Intern', 22000, '2023-06-20', 4),
('Nusrat Jahan', 'Business Analyst', 48000, '2022-11-11', 2),
('Sakib Rahman', 'DevOps Engineer', 53000, '2023-01-05', 3),
('Shamim Reza', 'Recruiter', 37000, '2022-12-12', 1);

UPDATE departments SET department_head_id = 1 WHERE department_id = 1;
UPDATE departments SET department_head_id = 2 WHERE department_id = 2;
UPDATE departments SET department_head_id = 3 WHERE department_id = 3;
UPDATE departments SET department_head_id = 4 WHERE department_id = 4;
