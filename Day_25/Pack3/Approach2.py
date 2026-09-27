## Example-- importing class from different (Modules and packages).
import std
## -----Logic given below-----

# Pack1- Emp(Employee)- display()-client
# Pack2- Std(student)- display()- client
# Pack3- client


# Package-Pack 1 and Pack2
# Modules- Emp(employees) and Std(Student)
# class- employees and Student
# Method- displayEmp() and displayStd()

from emp import Employee
empobj=Employee(102, "Shivam chauhan", 10)
empobj.displayemp()

from std import Student
stdobj=Student(101, "Shivk", 11)
stdobj.displaystd()

