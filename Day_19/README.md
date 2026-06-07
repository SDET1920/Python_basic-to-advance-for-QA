Python OOPs: Methods and Variables
Introduction

This project explains Object-Oriented Programming (OOPs) in Python, focusing on:

Methods
Types of methods
Variables (global, class, local)
Objects
1. Types of Methods in Python

Python supports mainly 3 types of methods:

1.1 Instance Method
Uses self
Works with object data
Called using object only
class ClassName:
    def method_name(self):
        pass
Example
class student:
    def method_name(self):
        print("Welcome to python")

s = student()
s.method_name()
1.2 Method with Parameters
class Student:
    def person(self, name):
        print("Student Name:", name)

s = Student()
s.person("Shiv")
1.3 Instance Method Example
class Student:
    def show(self):
        print("This is an instance method")

s = Student()
s.show()
2. Class Method
Uses cls
Works with class variables
Uses @classmethod
class Student:
    school = "Python school"

    @classmethod
    def school_name(cls):
        print(cls.school)

Student.school_name()
3. Static Method
Uses @staticmethod
No self or cls
Independent method
class Student:
    @staticmethod
    def greet():
        print("Hello python world")

Student.greet()
Static Method Example (Manual way)
class math:
    def addnumber(x, y):
        return x + y

math.addnumber = staticmethod(math.addnumber)

print("The Sum is:", math.addnumber(5, 10))
Better Way (Recommended)
class Math:
    @staticmethod
    def addnumber(x, y):
        return x + y

print("The Sum is:", Math.addnumber(20, 10))
4. Instance + Static Method Together
class myclass:
    def m1(self):
        print("This is instance method")

    @staticmethod
    def m2(num1, num2):
        print(num1, num2)

mc = myclass()
mc.m1()
mc.m2(11, 12)
5. Variables in Python OOP
5.1 Class Variables
class myclass:
    a, b = 10, 20

    def add(self):
        print(self.a + self.b)
5.2 Global, Class, and Local Variables
i, j = 10, 15   # global variable

class myclass:
    a, b = 10, 20  # class variable

    def add(self, x, y):  # local variables
        print(x + y)
        print(self.a + self.b)
        print(i + j)

my = myclass()
my.add(100, 200)
6. Multiple Objects in One Class
class myclass:
    def display(self, name):
        print("This is display method")
        print(name)

mc1 = myclass()
mc1.display("Welcome")

mc2 = myclass()
mc2.display("Shiv")
Conclusion

This project covers:

Instance methods
Class methods
Static methods
Global, class, and local variables
Object creation
Multiple objects usage

👉 Key Rule:

self → Instance method
cls → Class method
No self/cls → Static method