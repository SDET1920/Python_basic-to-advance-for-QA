Python Exception Handling

This repository contains simple Python examples to understand Exception Handling step by step.

Exception handling allows a Python program to handle errors gracefully instead of stopping the program unexpectedly.

📚 Topics Covered

In this repository, we will learn:

What is Exception Handling?

try block

except block

Handling specific exceptions

Multiple statements inside try

Raising our own exceptions using raise

Handling ValueError

Complete program flow after handling an exception

1. What is Exception Handling?

An exception is an error that occurs while a Python program is running.

For example:

print(10 / 0)


This produces:

ZeroDivisionError: division by zero


Without exception handling, the program stops when this error occurs.

Python provides try and except blocks to handle such errors.

Basic Syntax
try:
    # Code that may produce an exception
except:
    # Code that handles the exception

2. Example 1 — Basic Exception Handling
Code
print("This is starting point of program")
print("This is starting point of program")

try:
    print(x)

except:
    print("Exception handled")

print("This is end of program executed because the Exception error is handled....")
print("This is end of program executed because the Exception error is handled....")

Step-by-Step Explanation
Step 1 — Program starts
print("This is starting point of program")


Output:

This is starting point of program


The same statement is printed twice in the example.

Step 2 — Enter the try block
try:
    print(x)


Here, Python tries to execute:

print(x)


However, x has not been defined.

Therefore, Python raises:

NameError

Step 3 — except handles the exception
except:
    print("Exception handled")


Instead of allowing the program to stop, the except block handles the exception.

Output:

Exception handled

Step 4 — Program continues

After the exception is handled, Python continues executing the statements after the try-except block.

print("This is end of program executed because the Exception error is handled....")


Output:

This is end of program executed because the Exception error is handled....

Important Point

The main purpose of exception handling is:

Handle an error and allow the program to continue running when appropriate.

3. Example 2 — Handling a Specific Exception

In the previous example, we used a general except.

It is usually better to handle a specific exception when we know what error can occur.

Code
print("This is starting point of program")
print("Program in progress")

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Program successfully running and exception handled")

print("Program completed")

Step-by-Step Explanation
Step 1 — Program starts
print("This is starting point of program")


Output:

This is starting point of program

Step 2 — Program continues
print("Program in progress")


Output:

Program in progress

Step 3 — Code enters try
try:
    print(10 / 0)


Python tries to divide:

10 / 0


Division by zero is not allowed.

Python raises:

ZeroDivisionError

Step 4 — Specific exception is handled
except ZeroDivisionError:
    print("Program successfully running and exception handled")


Because the exception is ZeroDivisionError, this except block executes.

Output:

Program successfully running and exception handled

Step 5 — Program continues
print("Program completed")


Output:

Program completed

Why Use ZeroDivisionError?

Instead of writing:

except:


we can write:

except ZeroDivisionError:


This makes our exception handling more specific and easier to understand.

4. Example 3 — try, except, else, and finally

Python provides four useful keywords for exception handling:

try

except

else

finally

General Syntax
try:
    # Code that may cause an exception

except SomeException:
    # Code executed when exception occurs

else:
    # Code executed when no exception occurs

finally:
    # Code that executes whether exception occurs or not

Example
num1, num2 = 10, 5
result = num1 / num2

print("Result is:", result)

try:
    num3, num4 = 10, 0
    result = num3 / num4

    print("Result:", result)

except ZeroDivisionError:
    print("Program executed now")

Step-by-Step Explanation
Step 1 — Normal division
num1, num2 = 10, 5
result = num1 / num2


The calculation is:

10 / 5 = 2.0


Therefore:

print("Result is:", result)


Output:

Result is: 2.0

Step 2 — Enter try
try:
    num3, num4 = 10, 0
    result = num3 / num4


Python tries to calculate:

10 / 0


This causes:

ZeroDivisionError

Step 3 — Exception occurs

Because an exception occurs, Python does not execute:

print("Result:", result)


Instead, Python moves to:

except ZeroDivisionError:

Step 4 — Exception is handled
except ZeroDivisionError:
    print("Program executed now")


Output:

Program executed now

5. else Block

The else block executes only when no exception occurs inside the try block.

Example
try:
    num1 = 10
    num2 = 5
    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")
    print("Result:", result)


Output:

Division successful
Result: 2.0


Because no exception occurred, the else block executed.

6. finally Block

The finally block executes whether an exception occurs or not.

Example
try:
    num1 = 10
    num2 = 0
    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("This block always executes")


Output:

Cannot divide by zero
This block always executes


The finally block is commonly used for cleanup operations such as closing files or releasing resources.

7. Raising Our Own Exception

Python allows us to manually generate an exception using the raise keyword.

Code
def enterage(num):
    if num < 0:
        raise ValueError("check whether number negetive")

    if num % 2 == 0:
        print("Even numbers")
    else:
        print("Odd numbers")

    print("checking numbers is even or odd by calling function")


try:
    enterage(-1)

except ValueError:
    print("Value error exception occured and handled")

print("program completed")

8. Step-by-Step Explanation of raise
Step 1 — Create a function
def enterage(num):


The function accepts a number as an argument.

Step 2 — Check whether the number is negative
if num < 0:


If the number is less than zero, we don't want the function to continue.

Step 3 — Raise a ValueError
raise ValueError("check whether number negetive")


The raise keyword manually generates an exception.

Here we are generating:

ValueError

Step 4 — Call the function
try:
    enterage(-1)


The function receives:

-1


Since -1 < 0, the following code executes:

raise ValueError(...)

Step 5 — Handle the exception

The exception is handled by:

except ValueError:
    print("Value error exception occured and handled")


Output:

Value error exception occured and handled

Step 6 — Program continues

After handling the exception:

print("program completed")


Output:

program completed

9. Important Concept — raise

The raise keyword is useful when we want to create an exception ourselves based on a condition.

For example:

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")


This allows us to validate data and notify the caller when an invalid value is provided.

10. Complete Example

Here is a cleaner example combining try, except, else, and finally:

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division successful.")
    print("Result:", result)

finally:
    print("Program execution completed.")

Possible Output

If the user enters:

Enter first number: 10
Enter second number: 2


Output:

Division successful.
Result: 5.0
Program execution completed.


If the user enters:

Enter first number: 10
Enter second number: 0


Output:

Cannot divide by zero.
Program execution completed.

11. Exception Handling Flow

The basic flow can be understood like this:

             START
               |
               v
          +----------+
          |   try    |
          +----------+
               |
        Exception occurs?
          /          \
        Yes           No
         |             |
         v             v
    +---------+      else
    | except  |        |
    +---------+        |
         \             /
          \           /
           v         v
             finally
                |
                v
               END

12. Common Python Exceptions

Some commonly encountered Python exceptions are:

Exception	Meaning
ZeroDivisionError	Division by zero
ValueError	Invalid value
TypeError	Incorrect data type/operation
NameError	Variable or name is not defined
IndexError	Invalid list/sequence index
KeyError	Dictionary key does not exist
FileNotFoundError	File cannot be found
AttributeError	Object does not have the requested attribute
13. Best Practices
Use specific exceptions

Prefer:

except ZeroDivisionError:


instead of:

except:


Specific exception handling makes programs easier to understand and debug.

Keep the try block focused

Avoid putting a large amount of unrelated code inside try.

Instead of:

try:
    # lots of unrelated code


keep only the statements that may actually cause the expected exception.

Use meaningful error messages

For example:

raise ValueError("Age cannot be negative")


is clearer than:

raise ValueError("Error")

Don't silently ignore exceptions

Avoid empty exception handlers such as:

try:
    something()
except:
    pass


This can make debugging difficult.

14. Key Takeaways

try contains code that may cause an exception.

except handles an exception.

Specific exceptions such as ZeroDivisionError should generally be handled explicitly.

else runs when no exception occurs.

finally runs regardless of whether an exception occurs.

raise allows us to manually generate an exception.

ValueError is useful when a value is inappropriate or invalid.

Exception handling prevents appropriate runtime errors from unexpectedly terminating a program.
