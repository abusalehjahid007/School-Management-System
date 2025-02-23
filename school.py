
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
        
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self, subject, teacher):
        self.teachers[subject.name] = teacher
    
    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)
        
    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <=100:
            return 'A+'
        elif marks >= 70 and marks <= 79:
            return 'A'
        elif marks >= 60 and marks <= 69:
            return 'A-'
        elif marks >= 50 and marks <= 59:
            return 'B'
        elif marks >= 40 and marks <= 49:
            return 'C'
        elif marks >= 33 and marks <= 39:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.50,
            'D': 2.00,
            'F': 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value >= 4.50 and value <= 5.00:
            return 'A+'
        elif value >= 4.00 and value <= 4.49:
            return 'A'
        elif value >= 3.50 and value <= 3.99:
            return 'A-'
        elif value >= 3.00 and value <= 3.49:
            return 'B'
        elif value >= 2.50 and value <= 2.99:
            return 'C'
        elif value >= 2.00 and value <= 2.49:
            return 'D'
        else:
            return 'F'
        
    def __repr__(self):
        print("All Classrooms")
        for key in self.classrooms.keys():
            print(key)
            
        print("All Students")
        result = ''
        for key, val in self.classrooms.items():
            result += f"----{key.upper()} Classroom Students\n"
            for student in val.students:
                result += f"{student.name}\n"
        print(result)
        
        print("All Students Result")
        for key, val in self.classrooms.items():
            for st in val.students:
                for k,i in st.marks.items():
                    print(st.name, k, i, st.subject_grade[k])
                print(st.calculate_fial_grade())
        
        print("All Subjects")
        subject = ''
        for key, val in self.classrooms.items():
            subject += f"----{key.upper()} Classroom Subjects\n"
            for sub in val.subjects:
                subject += f"{sub.name}\n"
        print(subject)
        
        print("All Teachers")
        for subject_name, teacher in self.teachers.items():
            print(f"Subject: {subject_name}, Teacher: {teacher.name}") 
            
        return ""
    
        