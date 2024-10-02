# These are comments used for notes for ourselves or for other people reading our code. Comments are not outputted to the console window by the python interpreter. 

print("I love pizzas")
print("This is my 1st python program!")


# Variables in Python

# Strings

first_name = "Aanchal"
food = "pizza"
email = "aanchal@mad.com"

print(first_name)
#To use some text along with variables we have f-strings (aka formatted strings) this is similar to backticks in JS

print(f"My name is {first_name}")
print(f"{first_name}'s favourite food is {food}")

#Integers

age = 21
quantity = 3
num_of_students = 30

#Floats

price = 10.99
gpa = 9.52
distance = 5.5

#Booleans

is_student = True
for_sale = False
is_online = True

if is_online:
    print("you are online")
else:
    print("You are offline")


#Assignment Part
username = "aanchal__pahuja"
followers = 282
is_active = True
cgpa = 9.52


#Typecasting : using the 4 basic functions => str(), int(), float(), bool()

followers = float(followers)
print(followers)

cgpa = int(cgpa)
print(cgpa)

username = bool(username)
print(username)

marks = 10
marks = str(marks)

#type is used to check the datatype of the variable
print(type(marks))

marks += "1" #since marks is now a string variable. so it will be concatenated with 1 as a whole & it will produce the answer as 101
print(marks)


## user input 

name = input("Enter your name")
age = int(input("Please enter your age"))

print(f"Hello {name}")
print("Happy birthday")
age += 1
print(f"You are {age} yrs old now!")

## Exercise - 1: Calculate the area of the rectangle

length = float(input("Enter the length"))
width = float(input("Enter the width"))
area = length * width
print(f"Area of rectangle is {area}")

## Exercise - 1: Create a shopping cart program

item = input("What item would you like to buy?")
price = float(input("What is the price?"))
quantity = int(input("How many would you like?"))

total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"Your total is Rs. {total}")