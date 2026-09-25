Method Overriding in Python
What is Method Overriding?

Method overriding occurs when a child class provides its own implementation of a method that is already defined in the parent class.

When the overridden method is called using an object of the child class, the child class method is executed.

The parent class method can still be called from the child class using super().

Example: Method Overriding
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

A is the parent class.

B inherits from A.

Both classes have a method named m1().

The m1() method in class B overrides the m1() method in class A.

When obj.m1() is called, Python executes B.m1().

super().m1() calls the m1() method of the parent class A.

Important Points

Method overriding requires inheritance.

The child class defines a method with the same name as a method in the parent class.

When called through a child-class object, the child's implementation is used.

super() can be used to access the parent class implementation.

Method overriding is an important concept in runtime polymorphism.

Method Overriding vs Method Overloading
Method Overriding	Method Overloading
Requires inheritance	Does not necessarily require inheritance
Child class provides a new implementation of a parent method	Multiple methods with the same name but different parameters
Commonly used for runtime polymorphism	Python does not support traditional method overloading directly
super() can call the parent implementation	Default arguments or *args can be used to achieve similar behavior
Summary

Method overriding allows a child class to change or extend the behavior of a method inherited from its parent class.

class Parent:
    def show(self):
        print("Parent")


class Child(Parent):
    def show(self):
        print("Child")


obj = Child()
obj.show()


Output:

Child


Here, Child.show() overrides Parent.show().


