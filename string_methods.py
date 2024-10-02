#Validate username exercise: 
#1. username is no more than 12 characters
#2. username must not contain any spaces
#3. username must not contain any digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.find(" ") != -1:
    print("Your username can't contain any spaces")
elif not username.isalpha():
    print("Your username can't contain any digits")
else:
    print(f"Welcome {username}")  

## Rest of the methods usage is written in the notes. Kindly refer them!