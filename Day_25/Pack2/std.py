## Example-- importing class from different (Modules and packages).

## -----Logic given below-----

# Pack1- Emp(Employee)- display()-client
# Pack2- Std(student)- display()- client
# Pack3- client


# Package-Pack 1 and Pack2
# Modules- Emp(employees) and Std(Student)
# class- employees and Student
# Method- displayEmp() and displayStd()

class Student:
    def __init__(self,sid, sname, sgrad):
        self.sid=sid
        self.sname=sname
        self.sgrad=sgrad

    def displaystd(self):
        print(self.sid, self.sname, self.sgrad)