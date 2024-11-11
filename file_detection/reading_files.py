# Reading files in python (.txt, .json, .csv)

# Text files

file_path = "file_detection/output.txt"


try:   
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("This file does not exists!")
except PermissionError:
    print("You do not have permission to access this file!")
# JSON Files:

import json

file_path = "file_detection/file.json"

with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
    print(content["name"])

# CSV files:

import csv

file_path = "file_detection/collections.csv"

with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
        print(line)
        print(line[0])