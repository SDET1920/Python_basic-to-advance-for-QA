Python Date and Time Examples 🐍

A simple collection of Python examples demonstrating how to work with date and time using Python's built-in datetime module.

📌 Overview

This repository contains basic examples for:

Getting the current date and time

Getting only the current date

Accessing individual date and time components

Formatting date and time

These examples are suitable for beginners who are learning Python's datetime module.


📂 Examples
1. Get the Current Date and Time
from datetime import datetime

now = datetime.now()

print(now)


Example output:

2026-10-02 16:00:00.123456


The datetime.now() function returns the current local date and time.

2. Get Only the Current Date
from datetime import date

today = date.today()

print(today)


Example output:

2026-10-02


The date.today() function returns the current date without the time.

3. Get Individual Date and Time Components
from datetime import datetime

now = datetime.now()

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hours:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)


Example output:

Year: 2026
Month: 10
Day: 2
Hours: 16
Minute: 0
Second: 0


You can access individual components of a datetime object using attributes such as:

Attribute	Description
year	Current year
month	Current month
day	Current day
hour	Current hour
minute	Current minute
second	Current second

4. Format Date and Time
from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d-%m-%Y %H:%M:%S")

print(formatted)


Example output:

02-10-2026 16:00:00


The strftime() method is used to convert a date/time object into a formatted string.

Common Formatting Codes
Code	Meaning	Example
%d	Day	02
%m	Month	10
%Y	Four-digit year	2026
%H	Hour (24-hour format)	16
%M	Minute	00
%S	Second	00
