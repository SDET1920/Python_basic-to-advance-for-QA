JSON File Handling in Python

A simple Python project demonstrating how to create, read, update, and write JSON data using Python's built-in json module.

📌 Features

Create a JSON file (data.json)

Write data to a JSON file

Read JSON data from a file

Update existing JSON data

Save updated data back to the file

🛠️ Requirements

Python 3.x

No external libraries required

The project uses Python's built-in json module.

📂 Project Structure
.
├── data.json
├── main.py
└── README.md

🚀 How It Works
1. Create and Write JSON

The program creates data.json and stores the following data:

{
    "Name": "John",
    "age": 25
}

2. Read JSON Data

The JSON file is opened and its contents are loaded into a Python dictionary using json.load().

3. Update Data

The age value is changed from 25 to 35.

4. Save Updated Data

The updated dictionary is written back to data.json using json.dump().

The final data becomes:

{
    "Name": "John",
    "age": 35
}

💻 Example Code
import json

# Create/write JSON file
with open("data.json", "w") as file:
    json.dump({
        "Name": "John",
        "age": 25
    }, file)

# Read JSON
with open("data.json", "r") as file:
    data = json.load(file)

print(data)

# Update data
data["age"] = 35

# Write updated data back to file
with open("data.json", "w") as file:
    json.dump(data, file)

print(data)

📤 Expected Output
{'Name': 'John', 'age': 25}
{'Name': 'John', 'age': 35}

📚 Concepts Covered

Python dictionaries

JSON format

json.dump()

json.load()

File handling with open()

Reading and writing files

Updating JSON data
