## Variable--- it's two type global and local variable.

##Global variable- can define anywhere in code, outside of function.

## Local variable- We can define only inside of the fucntion.



## Write program with global variable

global_var=20
def fun():
    local_var=10
    print(local_var)
    print(global_var)
fun()                                  ## Both Global and local will be print.


## Now here global and local variable  will take by same name

xy=100
def fun():
    xy=101
    print(xy)
fun()                            ##here we take two variable by the same name so only local variable will be print...

## Now here global and local variable  will take by same name and print both variables.

xy=100
def fun():
    xy=101
    print("Let's Print the local variable inside function:", xy)
fun()
print("Let's Print the global variable outside function:", xy)  ##Now here it's done bcz we print out side of global variable.



###  Using Global variable in local variable and update values


xy=100
def fun():

    global xy
    xy=200                          ## Here xy is local variable but it's define global variable above.. "global xy" and update value.
    print(xy)
fun()
print(xy)



## Here we will diclare both global and local variable but will print only local

ab=101    #global variable
def fun():
    ab=102    #local variable
    print("Here we are print inside funcation local variable:", ab)     ## local variable is print
fun()


## Here we weill define global and local variable inside fucntion



def fun():
    ab = 100                 ##here variable ab=100, we used global xy and update value, xy=200
    global xy
    xy = 200
    print("Local variable", ab)              ## here if print ab then ab=100 will print or will print xy, so xy=200 will print

fun()
print("GLobal varialble:", xy)

