# Multi level inheritance

'''
class A():
    pass
    
class B(A):
    pass
    
class C(B):
    pass
'''
'''
class Student
    store student name
    store student marks
    english math nepali......marks are in tuple
class Marks
    calc percentange
    calc grade
class student profile
    student profile
'''
class Student():
    def __init__(self, name, **marks):
        self.name = name
        self.marks = marks
       
class Marks(Student):
    def percentage(self):
        total = 0
        for i in self.marks.values():
            total += i
        return total/len(self.marks)
   
    def grade(self):
        if self.percentage() >= 80:
            return "A"
        elif self.percentage() >= 60:
            return "B"
        elif self.percentage() >= 40:
            return "C"
        else:
            return "F"
       
       
class Student_profile(Marks):    

    def overallprofile(self):
        data = f'''
            Student Name: {self.name}
            Marks: {self.marks}
            Percentage: {self.percentage()}%
            Grade: {self.grade()}
            '''
        return data

   
total_subjects = int(input("Enter total number of subjects: "))
student_name = input("Enter student name: ")
student_marks = {}


for i in range(total_subjects):
    subject_name = input("Enter subject name: ")
    subject_marks = int(input(f'Enter  {subject_name} marks: '))
    student_marks[subject_name] = subject_marks
    print("-------------------------------")

obj = Student_profile(student_name, **student_marks)
print(obj.overallprofile())      