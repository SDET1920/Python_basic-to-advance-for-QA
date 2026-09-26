Python Calculator Module — Importing Functions

This project demonstrates three different approaches to importing and using functions from a Python module.

The example uses a simple calculator module containing add() and mul() functions.

📁 Project Structure
calculator-project/
│
├── calculator.py
└── main.py

🧮 Calculator Module

The calculator.py file contains two functions:

def add(num1, num2):
    print(num1 + num2)

def mul(num1, num2):
    print(num1 * num2)


These functions can be imported into another Python file in different ways.

1️⃣ Approach 1 — Import the Complete Module
import calculator

calculator.add(100, 200)
calculator.mul(10, 20)

Output
300
200


Here, the complete calculator module is imported. Functions are accessed using the module name:

calculator.add()
calculator.mul()

2️⃣ Approach 2 — Import Specific Functions
from calculator import add, mul

add(20, 20)
mul(10, 2)

Output
40
20


In this approach, only the required functions are imported from the calculator module.

You can directly call:

add()
mul()


without using the module name.

3️⃣ Approach 3 — Import Everything
from calculator import *

add(10, 5)
mul(10, 2)

Output
15
20


The * imports all names from the calculator module.

This allows the functions to be called directly:

add()
mul()


Note: Although this approach is possible, explicitly importing the functions you need is generally clearer and helps avoid name conflicts.

📊 Comparison
Approach	Syntax	Function Call
Import module	import calculator	calculator.add()
Import specific functions	from calculator import add, mul	add()
Import everything	from calculator import *	add()

🎯 Concepts Covered

Python modules

Creating and importing modules

import module

from module import function

from module import *

Calling functions from another Python file

📚 Conclusion

Python provides multiple ways to import functionality from modules. This example demonstrates the three common approaches:

Import the complete module.

Import specific functions.

Import all available names.

Understanding these approaches is an important step toward organizing Python programs into reusable modules.