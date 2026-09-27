Python Package Concept

This project demonstrates the Package Concept in Python using separate modules for Employee and Student.

The example shows how Python packages and modules can be used to organize and reuse code across different files.

📁 Project Structure
python-package/
│
├── main.py
│
└── mypackage/
    ├── __init__.py
    ├── emp.py
    └── std.py

📌 Package Concept

A package in Python is a directory containing Python modules. Usually, an __init__.py file is included to identify the directory as a Python package.

In this project:

mypackage is the package.

emp.py contains the Employee class.

std.py contains the Student class.

main.py imports and uses these classes.

👨‍💻 Employee Module

The emp.py module contains the Employee class.

Example:

class Employee:
    def __init__(self, empid, name, dept):
        self.empid = empid
        self.name = name
        self.dept = dept

    def displayemp(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.name)
        print("Department:", self.dept)

👨‍🎓 Student Module

The std.py module contains the Student class.

Example:

class Student:
    def __init__(self, rollno, name, standard):
        self.rollno = rollno
        self.name = name
        self.standard = standard

    def displaystd(self):
        print("Student Roll No:", self.rollno)
        print("Student Name:", self.name)
        print("Class:", self.standard)

▶️ Using the Package

The classes can be imported into main.py:

from mypackage.emp import Employee

empobj = Employee(102, "Shivam Chauhan", 10)
empobj.displayemp()

from mypackage.std import Student

stdobj = Student(101, "Shivk", 11)
stdobj.displaystd()

🖥️ Example Output
Employee ID: 102
Employee Name: Shivam Chauhan
Department: 10

Student Roll No: 101
Student Name: Shivk
Class: 11

🔑 Important Concepts
1. Module

A Python file containing classes, functions, or variables is called a module.

Examples:

emp.py
std.py

2. Package

A directory containing related Python modules is called a package.

Example:

mypackage/
├── __init__.py
├── emp.py
└── std.py

3. Import

The import statement allows us to use code from another module or package.

from mypackage.emp import Employee

🎯 Advantages of Packages

Organizes large Python projects.

Makes code easier to maintain.

Promotes code reusability.

Helps separate related functionality.

Avoids naming conflicts.

Makes modules easier to manage.

