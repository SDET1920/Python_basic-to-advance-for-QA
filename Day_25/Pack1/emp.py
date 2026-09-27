## Example-- importing class from different (Modules and packages).

## -----Logic given below-----

# Pack1- Emp(Employee)- display()-client
# Pack2- Std(student)- display()- client
# Pack3- client


# Package-Pack 1 and Pack2
# Modules- Emp(employees) and Std(Student)
# class- employees and Student
# Method- displayEmp() and displayStd()



class Employee:
    def __init__(self, eid, ename, esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def displayemp(self):
        print(self.eid,self.ename,self.esal)
