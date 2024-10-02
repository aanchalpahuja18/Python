# Python calculator

operator = input("Enter a valid operator (+ - / *): ")

num1 = float(input("Enter the value of the 1st num: "))
num2 = float(input("Enter the value of the 2nd num: "))

if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    result = num1 - num2
    print(result)
elif operator == '*':
    result = num1 * num2
    print(result)
elif operator == '/':
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator!")
