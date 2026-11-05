# Selenium Automation – Date Picker
📌 Project Overview

This project demonstrates how to automate Date Picker functionality using Python and Selenium WebDriver.

It covers selecting dates from different types of date pickers, including:

# jQuery UI Date Picker
Date Picker with Month and Year dropdowns
Selecting past and future dates
Navigating between months and years
Printing available dates in the console
Selecting a specific date dynamically


📂 Project Structure
text
DatePicker-Automation/
│
├── DatePicker.py
├── README.md


🌐 Websites Used for Practice
jQuery UI Date Picker
https://jqueryui.com/datepicker/
Dummy Ticket Date Picker
https://www.dummyticket.com/dummy-ticket-for-visa-application/

# 🚀 Date Picker Automation Scenarios
1. Selecting a Date Using send_keys()
Open the date picker.
Enter the required date directly into the input field.
Retrieve the entered date using get_attribute("value").

2. Selecting Date Using Previous and Next Buttons
Open the date picker.
Capture the displayed month and year.
Compare them with the required month and year.
Click Previous or Next until the required month and year appear.
Select the required date.

3. Selecting Date Using Month and Year Dropdowns
Open the date picker.
Select the required month using select_by_visible_text().
Select the required year using select_by_visible_text().
Retrieve all available dates using find_elements().
Print all available dates in the console.
Select the required date using a for loop.

# 💡 Selenium Concepts Covered
Selenium Concept	     Description
find_element()	         Locate a single web element
find_elements()	         Locate multiple web elements
click()                  Click on an element
send_keys()	             Enter text into an input field
get_attribute()	         Retrieve an element attribute
get_property()          	Retrieve a DOM property

Select	Handle dropdown elements
select_by_visible_text()	Select dropdown option by visible text
switch_to.frame()	        Switch to an iframe
.text	                    Retrieve visible text
while loop	                Navigate between months
for loop	                Iterate through available dates
break	                    Exit a loop


# After completing this project, you will understand:

How to handle different types of date pickers.
How to select dates dynamically using Selenium.
How to handle month and year dropdowns.
How to navigate between previous and future months.
How to work with iframes.
How to retrieve and print dates from a calendar.
How to use loops and conditional statements in Selenium automation.
