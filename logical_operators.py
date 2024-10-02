#Python - logical operator:

#1. or

temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The event is cancelled")
else:
    print("The event is still scheduled!")


#2. and & not

temp = -5
is_sunny = False

if temp > 25 and is_sunny:
    print("It is hot outside")
elif temp > 0 and temp < 25 and is_sunny:
    print("It is cold & weather is sunny outside!")
elif temp < 0 and not is_sunny:
    print("It's too cold outside")
else:
    print("Weather is cloudy and it is raining!")