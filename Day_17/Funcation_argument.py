## Two type of arguments/parameter we can pass to the function..


## 1- Positional argument.
## 2- Keyword argument.


### Define value where assigned to positional and keyword argument..

def fun(i,j):
    print(i,j)

fun(10,20)           ## it's Positional argument
fun(i=11, j=12)      ## it's keyword argument

## Define values assigned to possitional arguments....

def fun(i, j=9):
    print(i,j)

fun(100, 200)                ## here call the function and define values (100, 200) so it's print current values only.
                    ## One more thing here j=9 is default values which overridden by (200)..


## Another exaple for same..

def fun(i, j=2):
    print(i,j)
fun(3)                  ## here I only call one value so i=3 assigned and j=2 take default values so result (3,2)


## Another exmaple for same..

# def fun(i=21, j):
#     print(i,j)
# fun(19)                # Non-default arguments (required parameters) must come first
#                        # Default arguments (optional parameters) must come after them.



## Keyword arguement


def greeting(name, greetmsg):
    print(greetmsg+" "+name)

greeting(name="Shiv", greetmsg="hello")             ##Result- hello Shiv



## Example of default and non-default argument....


def fun(a,b,c):
    print(a,b,c)

fun(10,20,30)           ##Result-   10 20 30
fun(a=10, b=30, c=40)    ##Result-  10 30 40

fun(c=2,a=4,b=0)        ##Result-  4 0 2

fun(11,12,c=13)        ##Result- 11 12 13
fun(3,b=5,c=8)         ##Result- 3 5 8

fun(1,b=0,c=12)        ##Result- 1 0 12

#fun(10,b=2,c)         ##Syntax Error--This is wrong because positional arguments must appear before any keyword arguemnt.



## Find largest number using fun() in two numbers..

def largest(a,b):
    if a>b:
        return a
    else:
        return b
print(largest(100,200))
print(largest(20,10))


## Find largest numbers using fun() in three values

def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(largest(10, 20, 30))
print(largest(50, 20, 10))


## Using built-in max() (Best Way)

def largest(a, b, c):
    return max(a, b, c)

print(largest(10, 20, 70))



