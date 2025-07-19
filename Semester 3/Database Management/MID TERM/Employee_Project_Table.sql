CREATE DATABASE middummy;
USE middummy;

CREATE TABLE Employees (
	Employee_ID INT NOT NULL PRIMARY KEY,
    First_name VARCHAR(50) NOT NULL,
    Last_name VARCHAR(50) NOT NULL,
    Date_of_birth DATE,
    Department_ID INT NOT NULL,
    Salary INT
);

CREATE TABLE Projects (
	Project_ID INT NOT NULL PRIMARY KEY,
    Project_name VARCHAR(50) NOT NULL,
    Start_date DATE,
    End_date DATE,
    Budget INT
);

CREATE TABLE Employee_Projects (
    Employee_Id INT NOT NULL,
    Project_ID INT NOT NULL,
    PRIMARY KEY (Employee_Id, Project_ID),
    FOREIGN KEY (Employee_Id) REFERENCES Employees(Employee_Id),
    FOREIGN KEY (Project_ID) REFERENCES Projects(Project_ID)
);

    
    
    