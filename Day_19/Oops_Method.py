## Method-- Two types we can define in class

## 1-Instance method ( We can call only through object)

## 2- Static method (We can directly call using class)

## Ex-1- Simple program

class ClassName:
    def method_name(self):

        pass         ## Self refers to the current object of the class.

## EX-2-Simple Method

class student:
    def method_name(self):
        print("Welcome to python")

s= student()
s.method_name()

## Ex-3: Method with Parameters
class Student:
    def person(self, name):
        print("Student Name:", name)

s = Student()
s.person("Shiv")

## Type of Method..

# 1- Instance method()---Works with instance (object) variables and uses self.

class Student:
    def show(self):
        print("This is an instance method")

s = Student()
s.show()

# 2- Class method()-- Works with class variables and uses cls. Decorated with @classmethod.

class Student:
    school = "Python school"

    @classmethod
    def school_name(cls):
        print(cls.school)

Student.school_name()


## Ex 3- Static Method()--Does not use self or cls. Decorated with @staticmethod.

class Student:

    @staticmethod
    def greet():
        print("Hello python world")

Student.greet()


## Write a program using static method()

class math:
    def addnumber(x,y):
        return x+y

math.addnumber=staticmethod(math.addnumber)
print("The Sum is:", math.addnumber(5,10))

## Or better way to use always @staticemthod
# A static method:
# Does not use self.
# Does not use cls.
# Belongs to the class logically.
# Can be called directly using the class name.
# No object creation is required.  (in above code created a object)

class Math:
    @staticmethod
    def addnumber(x, y):
        return x + y

print("The Sum is:", Math.addnumber(20, 10))

##  Write other program

class myclass:
    def m1(self):
        print("This is instance method")

    @staticmethod
    def m2(self,num):

        print(self,num)


mc=myclass()
mc.m1()
mc.m2(11,12)

## Global variable//class variable//local variable example.

## Self is keyword that everytime represent class.

## Example- class variable.

class myclass:
    a, b=10, 20            ## a=10, b=20

    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

    def sub(self):
        print(self.b-self.a)

    def div(self):
        print(self.b/self.a)


mc=myclass()
mc.add()
mc.mul()
mc.sub()
mc.div()
print("All calculation operation Successfully done")


## Global/class/local variable example..

i,j=10, 15              #global variable.

class myclass:
    a,b=10,20              #class variable because within class.

    def add(self,x,y):       ##Create method here.
        print(x + y)         ## X and y local variable
        print(self.a+self.b)
        print(i+j)


my=myclass()
my.add(100,200)


## One class can have multiple objects...

class myclass:
    def display(self,name):
        print("This is display method")   ##This print you can add or remove.
        print(name)

mc1=myclass()
mc1.display("Welcome")

mc2=myclass()
mc2.display("Shiv")

