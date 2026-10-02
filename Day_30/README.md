Python Lambda Functions — Examples

A beginner-friendly collection of Python examples demonstrating lambda (anonymous) functions and their use with common Python functions such as sort(), filter(), and map().

📌 What is a Lambda Function?

A lambda function is a small anonymous function that can take any number of arguments but contains only one expression.

Syntax
lambda arguments: expression


For example:

square = lambda x: x * x

print(square(5))


Output:

25

📚 Examples
1. Square of Any Value

A lambda function can be used to calculate the square of a number.

square = lambda x: x * x

print(square(5))


Output:

25

2. Multiple Arguments

Lambda functions can accept multiple arguments.

add = lambda a, b: a + b

print(add(5, 20))


Output:

25

3. Using lambda with sort()

Lambda functions are commonly used as a key when sorting complex data.

student = [
    ("Alicia", 85),
    ("Bob", 72),
    ("Charlie", 91)
]

student.sort(key=lambda student: student[1])

print(student)


Output:

[('Bob', 72), ('Alicia', 85), ('Charlie', 91)]


Here, student[1] represents the student's marks, so the list is sorted according to the marks.

4. Using lambda with filter()

The filter() function is used to select items that satisfy a condition.

In this example, we filter out the even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


Output:

[2, 4, 6, 8]


The lambda function checks whether each number is divisible by 2.

5. Using lambda with map()

The map() function applies the same operation to every item in an iterable.

Here, every number is doubled.

numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: x * 2, numbers))

print(result)


Output:

[2, 4, 6, 8, 10, 12]

🧠 Quick Summary
Function	Purpose	Example
lambda	Create a small anonymous function	lambda x: x * x
sort()	Sort items	sort(key=lambda x: x[1])
filter()	Select items based on a condition	filter(lambda x: x % 2 == 0, numbers)
map()	Apply an operation to every item	map(lambda x: x * 2, numbers)

🎯 Learning Objectives

By going through these examples, you will learn:

What lambda functions are

How to create lambda functions

How to pass multiple arguments to a lambda

How to use lambda with sort()

How to use lambda with filter()

How to use lambda with map()

How anonymous functions can simplify small operations

📂 Project Structure
.
├── lambda_examples.py
└── README.md
