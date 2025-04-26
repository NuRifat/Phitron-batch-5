class Student:
    def __init__(self,name,cur_class,id):
        self.name = name
        self.cur_class = cur_class
        self.id = id
    def __repr__(self):
        return f'Student name is {self.name}, class - {self.cur_class} and id - {self.id}'
    
class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self):
        return f'Teacher name is {self.name}, subject - {self.subject} and id - {self.id}'
        
class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self,name,subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            return 'not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name,'python',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'
    
    def __repr__(self):
        print(f'Welcome to {self.name}')
        print('---------OUR TEACHERS---------')
        for teacher in self.teachers:
            print(teacher)
        print('---------OUR STUDENTS---------')
        for student in self.students:
            print(student)
        return 'All Done'

phitron = School('Phitron School')
phitron.enroll('Salman', 5000)
phitron.enroll('Sharuk', 8000)
phitron.enroll('Ranver', 20000)
phitron.enroll('Ranver', 7000)

phitron.add_teacher('Einstien','Physics')
phitron.add_teacher('Sakib','Algo')
phitron.add_teacher('Ashraful','Data Structure')
phitron.add_teacher('Tamim','Python')

print(phitron)