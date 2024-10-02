
num = -2
print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

a = 6
b = 7
max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age = 19
status = "Adult" if age >= 18 else "Child"
print(status)

temperature = 28
weather = "Hot" if temperature > 20 else "Cold"
print(weather)

user_role = "Guest"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level)