Python Method Overloading Examples

This repository demonstrates the concept of method overloading in Python using def

    def sayhello(self, name=None):
        if name is not None:
            print("Hello, " + name)
        else:
            print("hello")


h = Human()
 

h.sayhello("scott")ault arguments.

Python does not support traditional method overloading like Java or C++. Instead, similar behavior can be achieved using default parameter values, *args, or other techniques.

📌 Examples Included
1. Human Greeting Example

The Human class contains a sayhello() method with an optional name parameter.

class Human:
h.sayhello()

Output
Hello, scott
hello


The method behaves differently depending on whether a name is provided:

h.sayhello("scott") → Prints a personalized greeting.

h.sayhello() → Prints a general greeting.

2. Calculator Operation Example

The Calculation class demonstrates how default arguments can be used to perform addition with different numbers of arguments.

class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


obj = Calculation()

obj.add()
obj.add(10, 20)
obj.add(100, 200, 300)

Output
0
30
600


The same add() method can be called with different numbers of arguments:

Method Call	Result
obj.add()	0
obj.add(10, 20)	30
obj.add(100, 200, 300)	600

🧠 Key Concept
What is Method Overloading?

Method overloading means having multiple ways to call a method with different parameters.

In languages such as Java, you can define multiple methods with the same name but different parameter lists.

Python does not support this form of method overloading directly. If you define multiple methods with the same name in a class, the latest definition replaces the previous one.

Instead, Python commonly uses:

Default arguments

Variable-length arguments (*args)

Conditional logic

Example
def add(self, a=0, b=0, c=0):
    print(a + b + c)


Here, a, b, and c have default values of 0, allowing the method to be called with zero, two, or three arguments.

