## Constructor-- 1- The constructor name is fixed--   init(self):

## 2- Constructor never return any values.
## 3- Constructor can take argument/parameter.
## 4- Consructor will be called at the time of object creation itself.


## Write program with constructor.

class myclass:
    def __init__(self):
        print("This is constructor")

    def m1(self):
        print("hello")

    def m2(self, x, y):

        return(x+y)


mc=myclass()
mc.m1()
print(mc.m2(10,20))      ## we can print here x and y values or if you want use print then use print(x,y) before return.


## Create constructor by passing arguments..

class myclass:
    name="john"                    ## name= "john" is class variable..
    def __init__(self, name):
        print(name)
        print(self.name)
mc= myclass("Shiv")             ## "Shiv" is parameter

##  Requirement-- Create employee table and the below details can use to create Emp file.

## Constructor-- eid,enmae,sal

## Display-- print eid, ename, sal

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid,self.ename,self.sal)

e1=Emp(101,"shiv",5000)
e1.display()

e2=Emp(102,"kishor",6000)
e2.display()

##  Write code with use of string constructor __str__()

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def __str__(self):
        return str((self.eid, self.ename, self.sal))  #Yes, because __str__() is now returning a string so that the result will print

e1=Emp(103,"shiv kishor", 10000)
print(e1)