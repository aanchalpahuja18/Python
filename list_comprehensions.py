# List Comprehensions in Python


# Traditional Method
doubles = []

for value in range(1,11):
    doubles.append(value * 2)

print(doubles)

# By List Comprehensions

doubles = [x * 2 for x in range(1,11)]
print(doubles)

triples = [x*3 for x in range(1,11)]
print(triples)

squares = [x * x for x in range(1,11)]
print(squares)

# With strings

fruits = ["apple", "orange", "banana"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

fruits = [fruit[0] for fruit in fruits]
print(fruits)

# Using if conditions

nums = [-1,2,-3,4,-5,6,-7,8]

positive_nums = [num for num in nums if num >= 0]
negative_nums = [num for num in nums if num < 0]
even_nums = [num for num in nums if num % 2 == 0]
odd_nums = [num for num in nums if not num % 2 == 0]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]


passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
