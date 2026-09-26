# Polymorphis--- it's two type method overriding and method orverloading.


#  1- Method overiding-- When you have two methods with the same name, that each perform different task.

#  Where child class can provide the program with specific characterstics or specific implementaion procss of data provided that already define in parent/Super class.


# Example1- Calling parent class method using child class.

class A:
    def m1(self):
        print("This is m1 method from class A")

class B(A):
    def m1(self):
        print("This is m1 method from class B")
        super().m1()

obj=B()
obj.m1()

# Example 2- Method overriding example

class A:
    a,b=10,20

class B(A):
    i,j=100,200
    def m(self, x,y):
        print(x+y)
        print(self.i+self.j)
        print(self.a+self.b)

obj=B()
obj.m(1000,2000)

## Example 3- Overriding variable

class Parent:
    name= "scott"
class child(Parent):
    name= "john"

obj=child()
print(obj.name)


## Example 4- if you want print through overriding (Parent and class) value in same program.

class parent:
    name="scott"

class child(parent):
    name="john"

    def test(self):
        print(super().name)

obj=child()
print(obj.name)
obj.test()

## Example 4-- A parent bank have two bank one is x-bank other is Y-bank so here x bank return 10% rate of intrest to parent bank
# Y bank return 12% rate of intrest to parent bank.

# logic- X bank return rate of intrest 10% to parent bank.
# logic- Y bank return rate of intrest 12% to parent bank.

class bank:
    def rateofintrest(self):
        return 0
class xbank(bank):
    def rateofintrest(self):
        return 10
class ybank(bank):
    def rateofintrest(self):
        return 12

obj=xbank()
print(obj.rateofintrest())

obj=ybank()
print(obj.rateofintrest())
