# Writing data into (.txt, .csv, .json)

# Text file data insertion!
txt_data = "I love pizza"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} has been created!")


# JSON File data insertion

employees = {
    "name": "Aanchal",
    "title": "Student",
    "company": "GL",
    "pay": "5.66"
}

import json
file_path = "file.json"

try:
    with open(file_path, "w") as file:
        json.dump(employees, file, indent=4)
        print(f"json file {file_path} has been created")
except:
    print("File doesn't exists!")


# csv File data insertion


import csv

collection = [["Name", "Age", "Role"],
              ["Aanchal", 21, "Java Developer"],
              ["Parv", 17, "Student"],
              ["Riya", 43, "Administrator"],
              ["Praveen", 46, "Businessman"]]

file_path = "collections.csv"
try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in collection:
            writer.writerow(row)
        print(f"csv file {file_path} has been created")
except:
    print("File doesn't exists!")

