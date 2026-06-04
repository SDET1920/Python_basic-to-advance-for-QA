## Function-- A function set of statement which will perform a task.

## first program using function

def myfun():
    print("Hello learn python step by step")
myfun()         #called function for perform a task.


## write second program using function----pass value in function

def myfun(name):                            ## def--- defind function (def) is usded to diclare fucntion
    print("Hello", name)                   ## myfun-- it's function name which define
myfun("Shiv")                              ## name-- it is parameter or argument- any value passed to function..

## Write third program using function.----additin of two numbers using function

def cal(a,b):
    return (a+b)
result= cal(10,20)
print(result)


## Null value print using function

def fun():
    return
print(fun())                ##No value here passed so--- result is "none"

##  Write program to print "none" funcation value

def fun():
    i=10                    ## here return is not given so, it's printing none value
print(fun())


## if want to print then see the code.

def fun():
    i=10
    return i

print(fun())


## One more steps we can do the same.
def fun():
    i = 100000
    print(i)

fun()


## additing of two numbers using function..

def cal(a,b):
    print(a+b)
cal(2,5)


## or other method also to addition..

def cal(a,b):
    return (a+b)
print(cal(2,3))