import random

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # subject: teacher
        self.classrooms = {}  # name: ClassRoom object

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        self.classrooms[student.classroom.name].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80: return 'A+'
        elif marks >= 70: return 'A'
        elif marks >= 60: return 'A-'
        elif marks >= 50: return 'B'
        elif marks >= 40: return 'C'
        elif marks >= 33: return 'D'
        return 'F'

    @staticmethod
    def grade_to_value(grade):
        return {'A+': 5.0, 'A': 4.0, 'A-': 3.5, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}[grade]

    @staticmethod
    def value_to_grade(value):
        if value >= 4.5: return 'A+'
        elif value >= 3.5: return 'A'
        elif value >= 3.0: return 'A-'
        elif value >= 2.5: return 'B'
        elif value >= 2.0: return 'C'
        elif value >= 1.0: return 'D'
        return 'F'

    def show_all_students(self):
        for cname, croom in self.classrooms.items():
            print(f"\nClassroom: {cname}")
            for student in croom.students:
                print(f"- {student.name} (ID: {student.id})")

    def show_all_results(self):
        for cname, croom in self.classrooms.items():
            print(f"\nResults for {cname}:")
            for student in croom.students:
                for sub, mark in student.marks.items():
                    grade = student.subject_grade[sub]
                    print(f"{student.name} - {sub}: {mark} ({grade})")
                print(student.calculate_final_grade())

    def show_full_details(self):
        print(f"\nSchool Name: {self.name}")
        print(f"Address: {self.address}")
        print("\n--- Classrooms and Subjects ---")
        for cname, croom in self.classrooms.items():
            print(f"\nClassroom: {cname}")
            print("Subjects:", ', '.join([sub.name for sub in croom.subjects]))
            print("Students:")
            for student in croom.students:
                print(f"- {student.name} (ID: {student.id})")

class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        student.id = f"{self.name}-{len(self.students)+1}"
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.calculate_grade(mark)

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def evaluate_exam(self):
        return random.randint(30, 100)

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    def calculate_final_grade(self):
        if not self.subject_grade:
            return f"{self.name}'s grade not calculated."
        total = sum(School.grade_to_value(g) for g in self.subject_grade.values())
        gpa = total / len(self.subject_grade)
        self.grade = School.value_to_grade(gpa)
        return f"{self.name}'s Final Grade: {self.grade} (GPA: {gpa:.2f})"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

# ================= MAIN MENU =================

school = School("ABC School", "Dhaka")

def menu():
    while True:
        print("\n========== SCHOOL MANAGEMENT MENU ==========")
        print("1. Add Classroom with Subjects")
        print("2. Add Teacher")
        print("3. Admit Student")
        print("4. Take Exam for a Classroom")
        print("5. View All Students")
        print("6. View All Results")
        print("7. View Full School Details")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice == '1':
            cname = input("Enter classroom name: ")
            classroom = ClassRoom(cname)
            school.add_classroom(classroom)
            count = int(input("How many subjects to add?: "))
            for _ in range(count):
                sname = input("Subject name: ")
                tname = input("Teacher name for this subject: ")
                teacher = Teacher(tname)
                school.add_teacher(sname, teacher)
                subject = Subject(sname, teacher)
                classroom.add_subject(subject)
            print(f"Classroom '{cname}' added with {count} subject(s).")

        elif choice == '2':
            tname = input("Enter teacher name: ")
            sub = input("Enter subject taught: ")
            teacher = Teacher(tname)
            school.add_teacher(sub, teacher)
            print(f"Teacher {tname} added for subject {sub}.")

        elif choice == '3':
            sname = input("Enter student name: ")
            cname = input("Enter classroom: ")
            if cname in school.classrooms:
                student = Student(sname, school.classrooms[cname])
                school.student_admission(student)
                print(f"Student {sname} admitted to {cname}.")
            else:
                print("Classroom not found.")

        elif choice == '4':
            cname = input("Enter classroom name to take exam: ")
            if cname in school.classrooms:
                school.classrooms[cname].take_exam()
                print("Exams completed.")
            else:
                print("Classroom not found.")

        elif choice == '5':
            school.show_all_students()

        elif choice == '6':
            school.show_all_results()

        elif choice == '7':
            school.show_full_details()

        elif choice == '8':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
