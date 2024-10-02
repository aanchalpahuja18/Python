#Python - temperature conversion program

unit = input("Enter the unit in Fahrenheit or Celsius (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    unit = 'F'
    print(f"The temperature is now in {temp} {unit}")
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    unit = 'C'
    print(f"The temperature is now in {temp} {unit}")
else:
    print(f"The {unit} is not a valid unit of measurement")
    
