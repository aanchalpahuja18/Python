#While loops


#Example 1
name = input("Enter your name")
#Below will execute until user types a valid name & not an empty string!
while name == "":
    print("please enter your name")
    name = input("Enter your name")

print(f"Hello {name}")

#Example 2
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative!")
    age = int(input("Enter your age: "))
print(f"You are {age} yrs old!")

#Example 3 - Logical Operators inside while loop

food = input("Enter your fav food: (Press q to quit): ")

while not food == 'q':
    print(f"You like {food}")
    food = input("Enter your another fav food: (Press q to quit): ")
print("Okay Bye!")

#Example 4 - Logical Operators inside while loop

num = int(input("Enter a number between 1-10: "))

while num < 1 or num > 10:
    print("Your entered number is invalid!")
    num = int(input("Enter a number between 1-10: "))
print(f"Your number is {num}")
