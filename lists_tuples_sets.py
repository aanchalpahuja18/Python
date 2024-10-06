# Collections - A single variable used to store multiple values: There are 4 general purpose collections for beginners:

# Lists: Denoted by '[]'. Ordered & Mutable (can make changes). Duplicates are allowed. 

fruits = ["apple", "orange", "banana", "mango"]

# Below are common methods used for every collection in python till iterations
print(fruits)
# print(help(fruits))
# print(dir(fruits))
print("pineapple" in fruits)
print(len(fruits))
# for fruit in fruits:
#     print(fruit)

print(fruits[0])

# Methods specific to Lists:

#1. append()

fruits.append("pineapple")
print(fruits)

#2. sort()

fruits.sort()
print(fruits)

#3. reverse()
fruits.reverse()
print(fruits)

# 4. remove()

fruits.remove("pineapple")
print(fruits)

# 5. insert()

fruits.insert(0, "kiwi")
print(fruits)

# 6. index()
print(fruits.index("apple"))

# 7. count()

fruits.insert(0, "kiwi")
print(fruits.count("kiwi"))

# 8. clear()
fruits.clear()
print(fruits)

# Sets: Denoted by '{}'. Unordered & Immutable. But add/remove can be done. Also it cannot contain duplicates if tried to do so we will get only 1 value of the duplicate element in the set.

fruits = {"apple", "orange", "banana", "mango"}


#1. add()

fruits.add("pineapple")
print(fruits)

#2. remove()
fruits.remove("pineapple")
print(fruits)

#3. pop()
fruits.pop()
print(fruits)

# 4. clear()

fruits.clear()
print(fruits)

# Tuples: Denoted by '()'. They are ordered. They can contain duplicates. But they are immutable

fruits = ("apple", "orange", "banana", "mango", "apple")

#1. index()

print(fruits.index("apple"))

# print(dir(fruits))

#2. count()

print(fruits.count("apple"))

print(fruits[2])
print(fruits)