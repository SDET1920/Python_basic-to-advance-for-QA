# Selenium Python – Web Table Automation
# Project Overview

This project demonstrates Web Table handling using Selenium WebDriver with Python on the OrangeHRM demo application.

The main objective is to understand how to locate dynamic web table elements, count rows and columns, retrieve cell values, and validate user statuses using XPath.

1- Application Under Test
2- Application: OrangeHRM
3- URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
4- Module: Admin → User Management → Users
5- Browser: Google Chrome
6- Automation Tool: Selenium WebDriver
7- Programming Language: Python


# Login Credentials
Field	        Value
Username	    Admin
Password	   admin123

# Webtable- Test cases. 

1- Launching Chrome browser.
2- Navigating to the OrangeHRM application.
3- Login using valid credentials.
4- Navigating to the Admin module.
5- Capturing the total number of table rows.
6- Capturing the total number of table columns.
7- Verifying the webpage title.
8- Counting Enabled users.
9- Counting Disabled users.
10- Extracting table data using XPath.
11- Iterating through table rows using Python for loops.
12- Using find_element() and find_elements().

# XPath Locators Used
Description	XPath
Username	 //input[@name='username']
Password	 //input[@name='password']
Login Button	//button[@type='submit']
Admin Menu	//span[text()='Admin']
Table Rows	//div[@class='oxd-table-body']//div[@role='row']
Table Columns	(//div[@class='oxd-table-body']//div[@role='row'])[1]/div
Enabled Users	//div[@class='oxd-table-body']//div[text()='Enabled']
Disabled Users	//div[@class='oxd-table-body']//div[text()='Disabled']
Status Column	//div[@class='oxd-table-body']//div[@role='row']/div[5]


# 1. Counting Rows
python
Num_of_Rows = len(driver.find_elements(
    By.XPATH,
    "//div[@class='oxd-table-body']//div[@role='row']"
))

# 2. Counting Columns

Num_of_Columns = len(driver.find_elements(
    By.XPATH,
    "(//div[@class='oxd-table-body']//div[@role='row'])[1]/div"
))

# 3. Counting Enabled Users

enabled_count = len(driver.find_elements(
    By.XPATH,
    "//div[@class='oxd-table-body']//div[text()='Enabled']"
))

# 4. Counting Disabled Users

disabled_count = len(driver.find_elements(
    By.XPATH,
    "//div[@class='oxd-table-body']//div[text()='Disabled']"
))

# 5. Using For Loop to Count Enabled Users

count = 0

status_list = driver.find_elements(
    By.XPATH,
    "//div[@class='oxd-table-body']//div[@role='row']/div[5]"
)

for status in status_list:

    if status.text == "Enabled":
        count = count + 1

print("Number of Enabled Users:", count)

# Expected Output
Total Num of Rows: 24
Total Num of Columns: 6
Website Title: OrangeHRM
Enabled Users: 22
Disabled Users: 2

Number of Enabled Users: 22
Number of Disabled Users: 2


# Note: Actual results may change depending on the application's data and pagination.

Important Learning Points
Selenium Method	Purpose
find_element()	Locates a single web element
find_elements()	Locates multiple web elements
len()	Counts the number of elements
.text	Retrieves visible text
for loop	Iterates through multiple elements
XPath	Locates elements in the DOM
Difference Between find_element() and find_elements()
find_element() returns a single WebElement.
find_elements() returns a list of WebElements.
Use .text directly with a single element.
Use a loop to retrieve .text from multiple elements.
Project Learning Outcome

# After completing this project, you will understand:

How to automate dynamic web tables using Selenium Python.
How to capture rows and columns.
How to retrieve specific column values.
How to count Enabled and Disabled records.
How to construct dynamic XPath expressions.
How to use Python loops with Selenium WebElements.


