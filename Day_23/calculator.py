# Module-- A collection of function and class(variable+method) is called module.

# 1- A module can define function, class, and variable.
# 2- A module can also include runnable code.
# 3- Module can make code easier and understand.
# 4- import*- it's use to import all function.

## Example of Module- Suppose multiple developer working in software where developing different different module.


## Example 1- Calculator (Mathmatic operation with 3 different approach)

def add(num1, num2):
    print(num1+num2)

def mul(num1,num2):
    print(num1*num2)

add(100,200)
mul(10,20)

# Approach 1 for Example 1-
import calculator

calculator.add(100,200)
calculator.mul(10,20)

# Approach 2 for Example 1-

from calculator import add, mul

add(20,20)
mul(10,2)

# Approach 3 for Example 1-

from calculator import *

add(10,5)
mul(10,2)