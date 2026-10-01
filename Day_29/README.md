Python List Comprehension Examples 🐍

This repository contains simple examples of List Comprehension in Python.

List comprehension provides a concise way to create lists from an iterable such as range(), lists, strings, etc.

📚 Examples Included
Example 1 — Create Squares

Create a list of square numbers using list comprehension.

squares = [i * i for i in range(1, 6)]

print(squares)


Output:

[1, 4, 9, 16, 25]

Example 2 — Print Even Numbers

Find even numbers from 1 to 10 using a condition.

even = [i for i in range(1, 11) if i % 2 == 0]

print(even)


Output:

[2, 4, 6, 8, 10]

Example 3 — Even and Odd Using If-Else

Use if-else inside list comprehension to identify whether each number is even or odd.

result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 20)]

print(result)


Output:

['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',
 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',
 'Odd', 'Even', 'Odd']

Example 4 — Separate Even and Odd Numbers

Find and print even and odd numbers separately from 1 to 19.

numbers = range(1, 20)

even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

print(even)
print(odd)


Output:

[2, 4, 6, 8, 10, 12, 14, 16, 18]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

🧠 List Comprehension Syntax

The basic syntax of list comprehension is:

[expression for item in iterable]


With a condition:

[expression for item in iterable if condition]


With if-else:

[expression_if_true if condition else expression_if_false for item in iterable]

📌 What You Will Learn

These examples demonstrate:

Creating lists using list comprehension

Using range() with list comprehension

Performing calculations inside list comprehension

Using conditions with if

Using if-else

Finding even numbers

Finding odd numbers

Creating separate lists for even and odd numbers

📂 Project Structure
Python-List-Comprehension/
│
├── list_comprehension.py
└── README.md

