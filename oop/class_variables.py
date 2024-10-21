# Class Variables


class Student:
    
    year = 2025
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

    
student1 = Student("Aanchal", 21)
student2 = Student("Parv", 17)
student3 = Student("Riya", 43)
student4 = Student("Praveen", 46)

print(f"Our graduating year is {Student.year} & we have {Student.num_students} students in our class: ")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
