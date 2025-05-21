from school import *
from classroom import ClassRoom
from user import *
from subject import Subject

school = School('ABC', 'Dhaka')
eight = ClassRoom('Eight')
nine = ClassRoom('Nine')
ten = ClassRoom('Ten')

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rahim = Student("Rahim", eight)
karim = Student("Rahim", nine)
fahim = Student("Rahim", ten)
hahim = Student("Rahim", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hahim)

abul = Teacher("Abul khan")
babul = Teacher("Babul khan")
kabul = Teacher("Kabul khan")

bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chenistry = Subject("Chemistry", kabul)
biology = Subject("Biology", kabul)

eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chenistry)
nine.add_subject(biology)
nine.add_subject(physics)
nine.add_subject(chenistry)
nine.add_subject(chenistry)
ten.add_subject(bangla)
ten.add_subject(physics)
ten.add_subject(chenistry)
ten.add_subject(biology)

eight.take_semester_final()
nine.take_semester_final()
ten.take_semester_final()

print(school)
