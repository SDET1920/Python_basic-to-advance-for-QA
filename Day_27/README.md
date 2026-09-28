Python File Handling – Write, Read & Append

This project demonstrates the basic file handling operations in Python using a text file.

The program covers three fundamental file operations:

Write data into a text file

Read data from a text file

Append new data to an existing text file

📌 Concepts Covered
1. Write Operation

The file is opened using the "w" mode:

file = open("myfile.txt", "w")


The "w" mode creates a new file if it doesn't exist. If the file already exists, its previous contents are overwritten.

The program writes three lines:

This is my first file to write
This is my second file to write
This is my third file to write

2. Read Operation

The file is opened using the "r" mode:

file = open("myfile.txt", "r")
print(file.read())


The "r" mode is used to read the contents of an existing file.

3. Append Operation

The file is opened using the "a" mode:

file = open("myfile.txt", "a")


The "a" mode adds new content to the end of the existing file without deleting its previous contents.

The program appends:

This is my fourth line to append in earlier file
This is my fifth line to append in earlier file

📂 Project Structure
Day_27/
│
├── myfile.txt
├── file_handling.py
└── README.md


Replace file_handling.py with the actual Python filename used in your project.

🛠️ File Modes Used
Mode	Purpose
w	Write data and overwrite existing content
r	Read data from a file
a	Append data to the end of a file
💻 Complete Program
# Write data into the text file

file = open("myfile.txt", "w")

file.write("This is my first file to write \n")
file.write("This is my second file to write \n")
file.write("This is my third file to write \n")

file.close()

print("File handling program completed for: write")


# Reading data from myfile.txt

file = open("myfile.txt", "r")

print(file.read())

file.close()

print("Reading successfully done")


# Appending data into myfile.txt

file = open("myfile.txt", "a")

file.write("This is my fourth line to append in earlier file \n")
file.write("This is my fifth line to append in earlier file \n")

file.close()

print("Append is successfully done in earlier file")


🎯 Learning Objective

The purpose of this exercise is to understand the fundamentals of Python file handling, including opening, writing, reading, appending, and closing files.

📚 Topics

Python · File Handling · Read · Write · Append · Text Files · Python Basics