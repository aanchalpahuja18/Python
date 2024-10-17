#Iterables in Python

# List
fruits = ["apple", "mango", "banana"]

for fruit in fruits:
    print(fruit, end=" ")

print()

# Tuples
fruits = ("apple", "mango", "banana")

for fruit in reversed(fruits):
    print(fruit, end=" ")

print()

# Sets
fruits = {"apple", "mango", "banana"}

for fruit in fruits:
    print(fruit, end=" ")

print()

# Strings
name = "Aanchal Pahuja"

for char in name:
    print(char, end = " ")

print()

# Dictionary
my_dict = {"A": "1", "B": "2", "C": "3"}

for key in my_dict:
    print(key, end = " - ")