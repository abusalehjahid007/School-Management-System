from school import School
from person import Person, Teacher, Student
from subject import Subject
from classroom import Classroom

school = School("Phitorn", "Dhaka")


#For class Room
eight = Classroom("Eight")  
nine = Classroom("Nine")  
ten = Classroom("Ten")  

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#For Student
rahim  = Student("Rahim", eight)
karim  = Student("Karim", eight)
jarim  = Student("jarim", nine)
ashik  = Student("ashik", nine)
tashik  = Student("tashik", nine)
shofik  = Student("shofik", ten)
jabbar  = Student("Jabbar", ten)
sattar  = Student("Sattar", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(jarim)
school.student_admission(ashik)
school.student_admission(tashik)
school.student_admission(shofik)
school.student_admission(jabbar)
school.student_admission(sattar)

#For Teacher
abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
kabul = Teacher("kabul Khan")

#For Subject
bangla = Subject("Bangla", abul)
english = Subject("English", abul)
math = Subject("Math", kabul)
physics = Subject("Physics", kabul)
chemistry = Subject("Chemistry", babul)
biology = Subject("Biology", babul)


#add subject
eight.add_subject(bangla)
eight.add_subject(english)

nine.add_subject(math)
nine.add_subject(physics)

ten.add_subject(chemistry)
ten.add_subject(biology)


# Add teachers to the school
school.add_teacher(bangla, abul)
school.add_teacher(english, abul)
school.add_teacher(math, kabul)
school.add_teacher(physics, kabul)
school.add_teacher(chemistry, babul)
school.add_teacher(biology, babul)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)

