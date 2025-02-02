from person import Teacher
from school import School

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33
    
    def exam(slef, students):
        for student in students:
            mark = Teacher.evaluate_exam()
            student.marks[slef.name] = mark
            student.subject_grade[slef.name] = School.calculate_grade(mark)
            
            