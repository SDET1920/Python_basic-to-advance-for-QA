Polymorphism in Python

Polymorphism is one of the important concepts of Object-Oriented Programming (OOP).

The word Polymorphism means "many forms". In Python, polymorphism can be achieved in different ways, including:

Method Overriding

Method Overloading

This README focuses mainly on Method Overriding with practical Python examples.

1. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that is already defined in its parent class.

The method in the child class has the same name as the method in the parent class, but it can perform a different implementation.

Example 1: Calling the Parent Class Method Using super()
class A:
    def m1(self):
        print("This is m1 method from class A")


class B(A):
    def m1(self):
        print("This is m1 method from class B")
        super().m1()


obj = B()
obj.m1()

Output
This is m1 method from class B
This is m1 method from class A

Explanation

Here, class B inherits from class A and overrides the m1() method.

Inside B.m1(), we use:

super().m1()


The super() function is used to call the m1() method of the parent class A.

2. Method Overriding with Variables

Method overriding is commonly demonstrated with methods, but child classes can also define their own variables with the same name as variables in the parent class.

Example 2
class A:
    a, b = 10, 20


class B(A):
    i, j = 100, 200

    def m(self, x, y):
        print(x + y)
        print(self.i + self.j)
        print(self.a + self.b)


obj = B()
obj.m(1000, 2000)

Output
3000
300
30

Explanation

Class B inherits the variables a and b from class A.

It also defines its own variables:

i, j = 100, 200


The method m() can access both the child-class variables and the inherited parent-class variables.

3. Overriding a Variable

A child class can define a variable with the same name as a variable in its parent class.

In this case, the child class's variable takes precedence when accessed through an object of the child class.

Example 3
class Parent:
    name = "scott"


class Child(Parent):
    name = "john"


obj = Child()
print(obj.name)

Output
john

Explanation

Both classes contain a variable called name.

Parent:
    name = "scott"

Child:
    name = "john"


Since obj is an object of Child, Python uses the name defined in the Child class.

4. Accessing Parent and Child Variables Together

If we want to access both the child-class and parent-class values, we can use super() to access the parent-class variable.

Example 4
class Parent:
    name = "scott"


class Child(Parent):
    name = "john"

    def test(self):
        print(super().name)


obj = Child()

print(obj.name)
obj.test()

Output
john
scott

Explanation

When we write:

print(obj.name)


Python accesses the variable from the Child class:

john


Inside the test() method:

print(super().name)


super() accesses the parent class, so it prints:

scott

super() in Python

The super() function allows us to access members of the parent class from the child class.

For example:

super().m1()


calls a parent-class method.

Similarly:

super().name


accesses a parent-class variable.

Method Overriding vs Method Overloading
Feature	Method Overriding	Method Overloading
Classes involved	Parent and Child	Usually the same class
Method name	Same	Same
Purpose	Provide a different implementation in child class	Handle different arguments
Inheritance required	Yes	Not necessarily
Python support	Directly supported	Python does not support traditional method overloading like Java/C++
Method Overriding
class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")

Method Overloading in Python

Python does not support traditional method overloading where multiple methods with the same name can have different parameter lists.

Instead, developers commonly use default arguments, *args, or **kwargs.

Example:

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))


Output:

30
60

Key Points

Polymorphism means one interface or method name can have different forms or implementations.

Method overriding occurs when a child class provides a new implementation of a parent-class method.

super() can be used to access parent-class methods and variables.

A child class can define a variable with the same name as a parent-class variable.

Python does not provide traditional method overloading based solely on different parameter lists.

Default arguments, *args, and **kwargs can be used to achieve similar behavior.

Conclusion

Method overriding is an important OOP concept in Python. It allows a child class to customize or replace the behavior inherited from its parent class.

The super() function is especially useful when we want to access the original implementation or variables from the parent class.

class Parent:
    name = "scott"

    def show(self):
        print("Parent")


class Child(Parent):
    name = "john"

    def show(self):
        print("Child")
        super().show()


obj = Child()

print(obj.name)
obj.show()


This demonstrates how a child class can override parent behavior while still accessing the parent implementation when required.