🔎 Python Regex — ID Extraction from Text Files

A beginner-friendly Python project demonstrating how to use the built-in re module (Regular Expressions) to search for patterns and extract IDs from text and files.

This project covers re.search(), match.group(), and re.findall() with practical examples.

📌 What is Regex?

Regular Expression (Regex) is a pattern-matching technique used to search, locate, and extract specific information from text.

For example, given:

Order ID: ORD-12345


We can use:

r"ORD-\d+"


to extract:

ORD-12345

🧰 Python Module Used

This project uses Python's built-in re module:

import re


No external packages are required.

📂 Project Structure
regex-id-extraction/
│
├── data.txt
├── regex_examples.py
└── README.md

data.txt

Contains raw text data with different types of IDs, such as:

ORD-12345
CUST-10001
EMP-501
INV-20260001
TXN-900001
PROD-5001
TKT-70001

regex_examples.py

Contains different Regex examples for searching and extracting IDs.

🚀 Examples
Example 1 — Extract an Order Number
import re

text = "Order ID: ORD-12345"

match = re.search(r"ORD-\d+", text)

print(match.group())


Output:

ORD-12345

How It Works
ORD-12345
│   │
│   └── \d+ → one or more digits
└────── ORD- → literal text


re.search() searches the text for a matching pattern.

r"ORD-\d+" defines the Regex pattern.

match.group() returns the actual matched text.

📄 Example 2 — Read a File and Extract IDs

Instead of keeping the text directly inside Python, we can store it in data.txt.

import re

# Read text from file
with open("data.txt", "r") as file:
    text = file.read()

# Extract Order IDs
order_ids = re.findall(r"ORD-\d+", text)

print(order_ids)


Example output:

['ORD-12345', 'ORD-12346', 'ORD-12347', 'ORD-12348']

Why use re.findall()?

re.findall() returns all matches found in the text.

For example:

re.findall(r"ORD-\d+", text)


can return:

[
    "ORD-12345",
    "ORD-12346",
    "ORD-12347",
    "ORD-12348"
]

🆔 Example 3 — Extract Different Types of IDs

Different ID formats can have different Regex patterns.

import re

with open("data.txt", "r") as file:
    text = file.read()

order_ids = re.findall(r"ORD-\d+", text)
customer_ids = re.findall(r"CUST-\d+", text)
employee_ids = re.findall(r"EMP-\d+", text)
invoice_ids = re.findall(r"INV-\d+", text)
transaction_ids = re.findall(r"TXN-\d+", text)
product_ids = re.findall(r"PROD-\d+", text)
ticket_ids = re.findall(r"TKT-\d+", text)

print("Orders:", order_ids)
print("Customers:", customer_ids)
print("Employees:", employee_ids)
print("Invoices:", invoice_ids)
print("Transactions:", transaction_ids)
print("Products:", product_ids)
print("Tickets:", ticket_ids)


Example output:

Orders: ['ORD-12345', 'ORD-12346', 'ORD-12347', 'ORD-12348']

Customers: ['CUST-10001', 'CUST-10002', 'CUST-10003']

Employees: ['EMP-501', 'EMP-502', 'EMP-503', 'EMP-504']

Invoices: ['INV-20260001', 'INV-20260002', 'INV-20260003', 'INV-20260004']

Transactions: ['TXN-900001', 'TXN-900002', 'TXN-900003', 'TXN-900004']

Products: ['PROD-5001', 'PROD-5005', 'PROD-5012', 'PROD-5020']

Tickets: ['TKT-70001', 'TKT-70002', 'TKT-70003', 'TKT-70004']

🔍 Example 4 — Extract Almost Any ID

Instead of creating a separate Regex for every ID type, we can experiment with a more general pattern:

ids = re.findall(r"\b[A-Z]+(?:-[A-Z0-9]+)+\b", text)

print(ids)


This pattern can match IDs such as:

ORD-12345
CUST-10001
EMP-501
MGR-201
INV-20260001
TXN-900001
PROD-5001
TKT-70001
SHP-30001
WH-101
CR-501
REQ-450001
USER-9001
AUD-60001
TRK-IN-78451236
SKU-WM-1001
REPORT-20260928-001

Pattern Breakdown
\b[A-Z]+(?:-[A-Z0-9]+)+\b
│  │       │             │
│  │       │             └── End word boundary
│  │       └──────────────── One or more -section combinations
│  └──────────────────────── One or more uppercase letters
└─────────────────────────── Word boundary

Important Regex Symbols
Pattern	Meaning
\d	Any digit from 0–9
+	One or more
[A-Z]	Uppercase letter
[A-Z0-9]	Uppercase letter or digit
(?:...)	Non-capturing group
\b	Word boundary
r"..."	Raw Python string
🧠 Important Regex Functions
re.search()

Searches for the first match of a pattern.

match = re.search(r"ORD-\d+", text)

match.group()

Returns the actual text matched by the Regex.

print(match.group())


Output:

ORD-12345

re.findall()

Finds all matches and returns them as a list.

ids = re.findall(r"ORD-\d+", text)

🎯 Learning Goals

This project helps practice:

Regular Expressions

Python re module

re.search()

re.findall()

match.group()

File handling

Reading .txt files

Pattern matching

Extracting structured data from raw text

▶️ How to Run

Make sure Python is installed.

Run:

python regex_examples.py


The program will read data.txt and extract the IDs using different Regex patterns.

🧪 Practice Challenges

Try modifying the project to extract:

Tracking IDs

Warehouse IDs

Shipment IDs

API Request IDs

User IDs

Audit IDs

Reference Codes

SKU numbers

Multiple ID types using one Regex

Unique IDs without duplicates

For example:

unique_ids = set(ids)

for id in unique_ids:
    print(id)

📚 Key Takeaway

Regex is useful when working with unstructured text where you need to find specific patterns such as:

Order IDs
Customer IDs
Employee IDs
Invoice IDs
Tracking IDs
Transaction IDs
Product IDs
Ticket IDs


Python's re module provides a simple way to search, match, and extract this information.

⭐ Future Improvements

Possible improvements for this project:

Extract IDs from CSV files.

Extract IDs from JSON files.

Extract emails and phone numbers.

Extract dates and timestamps.

Remove duplicate IDs.

Save extracted IDs into a new file.

Create a reusable ID extraction function.

Build a small command-line Regex extractor.

Built with Python 🐍 and Regular Expressions 🔎