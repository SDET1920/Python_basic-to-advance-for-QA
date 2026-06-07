🐍 Python OOPs Concepts Playground

Learn Object-Oriented Programming in Python with simple, clean, and practical examples 🚀

📌 About This Project

This repository demonstrates Python OOPs fundamentals using real examples:

🧱 Classes & Objects
⚙️ Instance Methods
🏫 Class Methods
🔧 Static Methods
🌍 Global, Class & Local Variables
👥 Multiple Objects

Perfect for beginners + interview preparation.

🚀 Topics Covered
🧱 1. Instance Method

Uses self and works with object data.

class Student:
    def show(self):
        print("Welcome to Python")

s = Student()
s.show()
🧑‍🎓 2. Method with Parameters
class Student:
    def person(self, name):
        print("Student Name:", name)

Student().person("Shiv")
🏫 3. Class Method

Uses cls and class variables.

class Student:
    school = "Python School"

    @classmethod
    def school_name(cls):
        print(cls.school)

Student.school_name()
🔧 4. Static Method

No self or cls, independent method.

class Student:
    @staticmethod
    def greet():
        print("Hello Python Learner")

Student.greet()
➕ Static Method Example
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print("Sum:", Math.add(10, 20))
⚙️ 5. Instance + Static Together
class MyClass:
    def m1(self):
        print("Instance Method")

    @staticmethod
    def m2(a, b):
        print("Static Method:", a, b)

obj = MyClass()
obj.m1()
obj.m2(11, 12)
🌍 Variables in Python OOP
🧾 Class Variables
class MyClass:
    a, b = 10, 20

    def add(self):
        print(self.a + self.b)
🌐 Global + Class + Local Variables
i, j = 10, 15   # Global variables

class MyClass:
    a, b = 10, 20  # Class variables

    def add(self, x, y):  # Local variables
        print("Local:", x + y)
        print("Class:", self.a + self.b)
        print("Global:", i + j)

MyClass().add(100, 200)
👥 Multiple Objects Example
class MyClass:
    def display(self, name):
        print("Hello", name)

obj1 = MyClass()
obj2 = MyClass()

obj1.display("Welcome")
obj2.display("Shiv")

🧠 Key Takeaways
Concept	Meaning
self	Instance method reference
cls	Class method reference
No self/cls	Static method
Class variables	Shared across objects
Local variables	Inside method only