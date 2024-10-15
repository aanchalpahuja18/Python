# Functions - A set of reusable code

def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old now!")
    print("Happy Birthday to you!")

happy_birthday("Aanchal", 21)

print("----------------")
def invoice(username, amount, duedate):
    print(f"Hello {username}")
    print(f"You have an {amount} Rs. due on {duedate}")

invoice("aanchal", 100, "01/01")

def add(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

print("--------------")
print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

print("--------------")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("aanchal", "pahuja")

print(full_name)