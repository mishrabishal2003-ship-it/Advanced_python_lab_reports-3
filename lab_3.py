
                                           #LAB_3 Name: Bishal dubey Roll No: 07
# Creating Base class Employee and defining constructor with private variables and getter methods (encapsulation) and setter method for salary
class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    # Getter Methods
    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    # Setter Method
    def set_salary(self, salary):
        self.__salary = salary

# Defining Child class Professor that inherits the properties of base class Employee
class Professor(Employee):
    def __init__(self, emp_id, name, salary, subject):
        super().__init__(emp_id, name, salary)
        self.subject = subject

    def display_details(self):
        print("Professor Details")
        print("------------------")
        print("ID:", self.get_emp_id())
        print("Name:", self.get_name())
        print("Salary:", self.get_salary())
        print("Subject:", self.subject)

# Creating object of Professor (child) class
obj = Professor(11, "Harry", 90000, "Engineering Physics")
obj.display_details()


# Output:

# Professor Details
# ------------------
# ID: 11
# Name: Harry
# Salary: 90000
# Subject: Engineering Physics

# File Handling with CSV
import csv

data = [
    ['Name', 'Age', 'City'],
    ['Asha', 22, 'Kathmandu'],
    ['Ramesh', 25, 'Pokhara']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Using Pandas Library (CSV)
import pandas as pd

data = {
    'Name': ['Asha', 'Ramesh'],
    'Age': [22, 25],
    'City': ['Kathmandu', 'Pokhara']
}

df = pd.DataFrame(data)
df.to_csv('output1.csv', index=False)

# Reading CSV File
with open('output.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading CSV using Pandas
output = pd.read_csv('output.csv')
print(output)

# File Handling with JSON
import json

data = [
    {"Name": "Asha", "Age": 22},
    {"Name": "Ramesh", "Age": 25}
]

with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)

# File Handling with TXT
students = [
    "1, Ram, 85",
    "2, Sita, 90",
    "3, Hari, 78"
]

with open("students.txt", 'w') as file:
    for student in students:
        file.write(student + "\n")

# Reading TXT File
with open("students.txt", "r") as file:
    content = file.read()

print("Reading data from file:")
print(content)

# Creating Data and Writing to Excel
import pandas as pd

data = {
    "ID": [1, 2, 3],
    "Name": ["Ram", "Sita", "Hari"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)

# Reading Excel File
df = pd.read_excel("students.xlsx")
print(df)
