USE assignment1;

CREATE TABLE Student(
	Roll INT NOT NULL PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    Class INT,
    Section ENUM('Science','Commerce','Arts'),
    Age INT CHECK (Age >= 10)
);

CREATE TABLE Library(
	BookID INT NOT NULL PRIMARY KEY,
    BookName VARCHAR(30),
    StudentRoll INT NOT NULL,
    FOREIGN KEY(StudentRoll) references Student(Roll)
);

CREATE TABLE Fees(
	Fee INT CHECK (Fee>0),
    StudentRoll INT NOT NULL,
    StudentName VARCHAR(30),
    FOREIGN KEY(StudentRoll) references Student(Roll)
);