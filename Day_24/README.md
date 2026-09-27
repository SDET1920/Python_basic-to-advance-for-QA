Python Packages and Modules

This project demonstrates how to create and import Python modules from a package directory.

📁 Project Structure
Day_24/
│
├── Pack1/
│   ├── __init__.py
│   ├── Module1.py
│   └── Module2.py
│
└── main.py

📌 What Are Python Modules?

A module is a Python file (.py) containing functions, classes, or variables that can be reused in other Python programs.

For example:

# Module1.py

def display():
    print("This is Module 1")

# Module2.py

def show():
    print("This is Module 2")

📦 What Is a Python Package?

A package is a directory containing Python modules. Traditionally, a package contains an __init__.py file that tells Python that the directory can be treated as a package.

Example:

Pack1/
├── __init__.py
├── Module1.py
└── Module2.py


Here, Pack1 is the package, while Module1 and Module2 are modules.

🚀 Importing Modules

The modules can be imported into another Python file using import.

import sys

sys.path.append(
    "C:/Users/hp/PycharmProjects/Python_basic-to-advance-for-QA/Day_24/Pack1"
)

import Module1
import Module2

Module1.display()
Module2.show()

How It Works

sys is imported to access Python's system-related functionality.

sys.path.append() adds the Pack1 directory to Python's module search path.

Module1 and Module2 are imported.

The functions display() and show() are called using the module names.

⚠️ Recommended Approach

Instead of adding an absolute path with sys.path.append(), it is generally better to structure the project as a package and use package imports.

For example:

from Pack1 import Module1
from Pack1 import Module2

Module1.display()
Module2.show()


This makes the project easier to move between computers and share on GitHub.

🧪 Example Output
This is Module 1
This is Module 2

🎯 Learning Objectives

By completing this example, you will understand:

What a Python module is

What a Python package is

The purpose of __init__.py

How to import modules

How to call functions from imported modules

The purpose of sys.path

Why package-based imports are preferable to hard-coded paths


📚 Key Concepts
Concept	Description
Module	A Python .py file containing reusable code
Package	A directory containing related Python modules
__init__.py	Traditionally used to identify a Python package
import	Used to import modules or packages
sys.path	Contains locations where Python searches for modules
from ... import ...	Imports a specific module or object

