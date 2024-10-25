# Class Methods in Python

class Student:

    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no. of students: {cls.count}"
    
    @classmethod
    def get_gpa(cls):
        if cls == 0:
            return 0
        else:
            return f"Average gpa is: {cls.total_gpa / cls.count}"
    

student1 = Student("Aanchal", 9.52)
student2 = Student("Parv", 9.67)
student3 = Student("Riya", 9.66)

print(Student.get_count())
print(Student.get_gpa())