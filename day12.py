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
    def printDetails(self):
        details = f"Name: {self.name}\n"
        for subject, mark in self.marks.items():
            details += f"  {subject}: {mark}\n"
        details += f"Total Percentage: {self.percentage():.2f}%\n"
        details += f"Grade: {self.grade()}"
        return details
   
 
def get_input():
    name = input("Enter your name: ")
    marks={}
    for _ in range(3):
        sub = input("Enter subject name: ")
        mark = int(input("Enter marks: "))
        marks[sub] = mark
       
    return name, marks
 
name, marks = get_input()
student = Student_profile(name, **marks)
print(student.printDetails())
        