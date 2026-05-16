#Formating.

#Example 1- One way.

name= "shiv"
age= 28
sal= 60000

print(name)
print(age)
print(sal)

#Example 2- Second way

name,age,sal="shiv", 28, 600000
print(name,age,sal)

#Example 3- Third way

name= "shiv"
age=28
sal=50

print("Name is:",name)
print("Age is:",age)
print("salary is:",sal)

#Example 4- Fourth way.

print("Name is: %s, Age is:%d, salary is:%g" %(name,age,sal))   #(S is string,d is digit, g is decimal)


#Example 5- fifth way- Better Modern Method-Use f-string:

print(f"Name is: {name}, Age is: {age}, Salry is: {sal}")

#Example 6- sixth way--

print("Name is: {}, Age is: {}, Salary is: {}".format(name,age,sal))
