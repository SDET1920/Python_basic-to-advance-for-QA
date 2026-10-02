# Regex-- It help with locating dynamic element and extracting text attribute.

# re.search()-- Search for pattern through text.
# match.group()- Give us the actual text the match regax.
# re.findall()- Extract multple values from text.


# Example 1-  Extracting order number from text.


import re

text= "Order ID: ORD-12345"

match=re.search(r"ORD-\d+", text)

print(match.group())


# Example 2-  Read the file in Python and extract ORD- id's from raw text data.

import re

# Read text from file
with open("data.txt", "r") as file:
    text = file.read()

# Extract Order IDs
order_ids = re.findall(r"ORD-\d+", text)

print(order_ids)

#Output: ['ORD-12345', 'ORD-12346', 'ORD-12347', 'ORD-12348', ...]

#Example 3. Extract different types of IDs- You can create separate patterns:

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


# Example 4-- Extract almost any ID- You can also experiment with a more general pattern:

ids = re.findall(r"\b[A-Z]+(?:-[A-Z0-9]+)+\b", text)

print(ids)



