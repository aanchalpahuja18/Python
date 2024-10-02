#Arithmetic operators

x = 3.14
y = 4
z = 5

#1. Addition

x = x + 1
x += 1 # This is known as augmented assignment operator in python

#2. Subtraction

x = x - 1
x -= 1 # This is known as augmented assignment operator in python

#3. Mulitiplication

x = x * 1
x *= 1 # This is known as augmented assignment operator in python

#4. Division

x = x / 1
x /= 1 # This is known as augmented assignment operator in python

#5. Remainder operator aka Modulo Operator

x = x % 2

#6. power operator or exponent operator

x = x ** 2
x **= 2

## Built in Math functions

#1. round()
result = round(x)

#2. abs()
p = -2
result = abs(p)

#3. pow()
result = pow(4,2)

#4. max()
result = max(x, y, z)

#5. min()
result = min(x, y, z)

## Useful constants & function from math class

import math

#1. math.pi
print(math.pi)

#2. math.e
print(math.e)

#3. math.sqrt
print(math.sqrt(9))

#4. math.ceil
print(math.ceil(9.1))

#5. math.floor
print(math.floor(9.9))

#Exercises:

#1. We want to calculate the circumference of a circle:

# radius = float(input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# print(f"Circumference of the circle is: {circumference}")

#2. We want to calculate the area of a circle:

# radius2 = float(input("Enter the radius of the circle: "))
# area = math.pi * pow(radius2, 2)
# print(f"Area of the circle is: {round(area,2)}")

#3. We want to calculate the hypotenuse of a right angled triangle:

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f"Hypotenuse of a right angled triangle is: {c}")
