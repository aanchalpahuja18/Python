# Arbitrary Arguments: We can pass any no of arguments to our functions, These can be handled by *args & **kwargs.

#1. *args:

def add(*args):
    total = 0
    for arg in args:
        total+= arg
    return total

print(add(1,2,3,4,5))

#2. kwargs:

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_address(street = "Hiwari", 
#               apt = "60",
#               city = "Nagpur",
#               state = "Mah",
#               zip = "440008")

#3. args & kwargs together example

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")

    print()

    for key,value in kwargs.items():
        print(f"{key}: {value}")


shipping_label("Ms.", "Aanchal", "Pahuja",
               street = "Hiwari", 
              city = "Nagpur",
              state = "Mah",
              zip = "440008")