# Membership Operators in Python

word = "APPLE"

letter = input("Enter a letter: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"No {letter} was found!")


students = {"Aanchal", "Pari", "Riya"}

student = input("Enter a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print("No valid student found")


grade = {"Aanchal": "A", "Pari": "B", "Riya": "C"}

student = input("Enter a student: ")

if student in grade:
    print(f"{student}'s grade is : {grade[student]}")
else:
    print("No valid student found")


email = "aanchal@gmail.com"

if "@" in email and "." in email:
    print("valid email!")
else:
    print("Invalid email")