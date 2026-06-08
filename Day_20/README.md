📘 Python OOP - Constructor & Class Examples

This project demonstrates basic Object-Oriented Programming (OOP) concepts in Python such as:

Constructor (__init__)
Instance Methods
Class Variables
Returning values from methods
String representation using __str__()
📌 1. What is a Constructor?
✔ Definition:

A constructor is a special method in Python:

__init__(self)
✔ Features:
Automatically called when an object is created
Used to initialize variables
Can take parameters
Does not return any value
🧪 Example 1: Constructor + Methods
class myclass:
    def __init__(self):
        print("This is constructor")

    def m1(self):
        print("hello")

    def m2(self, x, y):
        return (x + y)

mc = myclass()
mc.m1()
print(mc.m2(10, 20))
🔹 Output:
This is constructor
hello
30
🧠 Explanation:
Constructor runs automatically
m1() prints message
m2() returns sum of two numbers
🧪 Example 2: Constructor with Parameters + Class Variable
class myclass:
    name = "john"   # Class variable

    def __init__(self, name):
        print(name)        # Parameter value
        print(self.name)   # Class variable

mc = myclass("Shiv")
🔹 Output:
Shiv
john
🧠 Explanation:
"Shiv" is passed as argument
self.name refers to class variable "john"
🧪 Example 3: Employee Class using Constructor
class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print(self.eid, self.ename, self.sal)

e1 = Emp(101, "shiv", 5000)
e1.display()

e2 = Emp(102, "kishor", 6000)
e2.display()
🔹 Output:
101 shiv 5000
102 kishor 6000
🧠 Explanation:
Each object stores its own employee data
display() prints object data
🧪 Example 4: Using __str__() Constructor
class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return str((self.eid, self.ename, self.sal))

e1 = Emp(103, "shiv kishor", 10000)
print(e1)
🔹 Output:
(103, 'shiv kishor', 10000)

🧠 Explanation:
__str__() defines how object is printed
It must return a string
print(e1) automatically calls __str__()
📌 Key Points Summary
__init__() → Constructor (runs automatically)
self → refers to current object
Constructors do NOT return values
Methods can return values
__str__() is used for readable object output
Class variables are shared among all objects
Instance variables are unique to each object