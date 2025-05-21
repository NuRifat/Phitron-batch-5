import random
from school import *


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}  # {"Eng":70,"ICT":90}
        self.subject_grade = {}  # {"Eng": 'A'}
        self.garde = None  # final grade

    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_grade.values():
            grade_point = School.grade_to_value(grade)
            sum += grade_point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = sum/len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final grade : {self.grade} with GPA = {gpa}"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
