USE rifatlearningdb;

-- 4 table create (Instructor, Course, Enrollment, Student)
CREATE TABLE Instructor (	
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15),	
    Department VARCHAR(50)	
);	
CREATE TABLE Course (	
    CourseID INT AUTO_INCREMENT PRIMARY KEY,	
    Title VARCHAR(255) NOT NULL,	
    Credits INT NOT NULL,	
    InstructorID INT,	
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)	
);	
CREATE TABLE Student (	
    StudentID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15)	
);
CREATE TABLE Enrollment (	
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,	
    StudentID INT,	
    CourseID INT,	
    EnrollmentDate DATE NOT NULL,	
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),	
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)	
);	

-- question ans:

-- insert a new enrollment record for a student (e.g., StudentID 5) into the course with the highest credit hours,
INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate)
VALUES (
    5,
    (
        SELECT CourseID
        FROM Course
        ORDER BY Credits DESC
        LIMIT 1
    ),
    CURRENT_DATE()
);
-- assign a new instructor to a course (e.g., CourseID 3) by updating the InstructorID,
UPDATE Course
SET InstructorID = 7
WHERE CourseID = 3;
-- SQL query to find the names of instructors who teach the most credits (total),
SELECT Name
FROM Instructor
WHERE InstructorID = (
    SELECT InstructorID
    FROM Course
    GROUP BY InstructorID
    ORDER BY SUM(Credits) DESC
    LIMIT 1
);
-- SQL query to list all students who are enrolled in more than two courses,
SELECT StudentID, COUNT(*) 
FROM Enrollment
GROUP BY StudentID
HAVING COUNT(*) > 2;

-- SQL query using ON DELETE CASCADE on Course so that all courses are deleted when an instructor is removed,
CREATE TABLE Course (
	CourseID int NOT NULL PRIMARY KEY,
	Course_Name VARCHAR(30),
	Credits int,
	InstructorID int,
	FOREIGN KEY(InstructorID) REFERENCES Instructor(InstructorID)
	ON DELETE CASCADE
);

