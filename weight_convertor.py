#Python weight convertor program

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K, L): ")

print("Your conversion of weight is in process...")
if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f"Your weight is : {weight} {unit}")
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kg.'
    print(f"Your weight is : {weight} {unit}")
else:
    print(f"{unit} is not a valid unit")

