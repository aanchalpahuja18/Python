# File Detection in Python


import os

file_path = "file_detection\\test.txt"

if os.path.exists(file_path):
    print(f"The location of the {file_path} exists")
    if os.path.isfile(file_path):
        print("It is a file!")
else:
    print("The location does'nt exists")