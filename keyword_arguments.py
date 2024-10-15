# Positional Arguments

def hello(greetings, title, first, last):
    print(f"{greetings} {title}{first} {last}")


hello("Hello", "Ms.", last = "Pahuja", first = "Aanchal")

print("1", "2", "3", "4", "5", sep = "-")

def country_code(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = country_code("+91", first = "2281", last = "3669", area = "90")

print(phone_num)