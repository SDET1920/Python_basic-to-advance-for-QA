## Example-- importing class from different (Modules and packages).

## -----Logic given below-----

# Pack1- Emp(Employee)- display()-client
# Pack2- Std(student)- display()- client
# Pack3- client


# Package-Pack 1 and Pack2
# Modules- Emp(employees) and Std(Student)
# class- employees and Student
# Method- displayEmp() and displayStd()

import sys

sys.path.append("C:/Users/hp/PycharmProjects/Python_basic-to-advance-for-QA/Day_25/Pack1")
sys.path.append("C:/Users/hp/PycharmProjects/Python_basic-to-advance-for-QA/Day_25/Pack2")

import emp

empobj = emp.Employee(101, "Shiv", 5000)
empobj.displayemp()

import std

stdobj = std.Student(111, "Kishor", "A")
stdobj.displaystd()
