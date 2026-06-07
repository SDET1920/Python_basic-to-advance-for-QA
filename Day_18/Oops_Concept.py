## Oops concept in python-
## 1-Python is structural and Oops base language.
## 2- We can write program without class or with class, but in Java always class is required bcz java is pure Oops based.

## Class- Collection of variables, logical entity, does not occupy space in the memory..

## Object- Object is instance of class, physical entity, Occupy certain ammount of space in memory


## Write program to create a class.

class myclass:
    x=5

print(myclass)

## write program to create class with object.
class myclass:          ## Class is define
    x=5
print(myclass)

p1 = myclass()          ## Object is created.
print(p1.x)

## Write program to create class with object..

class myclass:       ### class created
    def myfun(self):          ## function/method created self.
        pass                  ## no values here
    def display(self):            ## function create and print values
        print("Shiv is doing coding")

mc=myclass()                        ## Create object and store a close
mc.myfun()                          ## Call myfun here is no values so nothing will print.
mc.display()                        ## call display here is value "shiv is doing coding" print in console.



## Write program to print name using class and object..

class myclass:
    def fun(self):
        print("Hello Oops concept in python")

m=myclass()
m.fun()
