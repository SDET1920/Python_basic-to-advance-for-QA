# Exceptioinhandling-- it's a way to handle errors that occur, which a program is running so the program can respond
# gracefull instead of crash.

# Example 1-- Exception handling

print("This is starting point of program")
print("This is starting point of program")

try:
  print(x)

except:
  print("Exception handled")

print("This is end of program executed because the Exception error is handled....")
print("This is end of program executed because the Exception error is handled....")

# Example 2- Exception handling

print("This is starting point of program")
print("Program in progress")

try:
  print(10 / 0)

except ZeroDivisionError:
    print("Program successfully running and exception handled")

print("Program completed")

## Example 3--- Multiple exception blocks- try, except, else, finally.

num1, num2= 10, 5
result= num1/num2

print("Result is:", result)            ## Result is: 2.0

try:
    num3, num4= 10, 0
    result= num3/num4

    print("Result:", result)             ## ZeroDivisionError: division by zero

except ZeroDivisionError:
    print("Program executed now")


## Raising our own exception.

def enterage(num):
    if num<0:
        raise ValueError("check whether number negetive")

    if num%2==0:
        print("Even numbers")
    else:
        print("Odd numbers")

    print("checking numbers is even or odd by calling function")

try:
    enterage(-1)
except ValueError:
    print("Value error exception occured and handled")
print("program completed")


