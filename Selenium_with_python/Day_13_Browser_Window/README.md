# Handling Browser Windows in Selenium Python
1. Introduction

This project demonstrates how to handle multiple browser windows in Selenium WebDriver using Python.

Selenium provides methods to switch between parent and child browser windows, retrieve window IDs, and close specific browser windows.

# Important Selenium Methods
Method-----	                      Description------
driver.window_handles	          Returns IDs of all open browser windows.
driver.current_window_handle	  Returns the ID of the current browser window.
driver.switch_to.window(id)	      Switches to a specific browser window.
driver.title	                  Returns the title of the current browser window.
driver.close()	                  Closes the current browser window.
driver.quit()	                  Closes all browser windows and ends the session.

# Handling Multiple Browser Windows
Example 1: Get Parent and Child Window IDs
python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(3)

windowsids = driver.window_handles

Parent_Window_Id = windowsids[0]
Child_Window_Id = windowsids[1]

print("Parent Window ID:", Parent_Window_Id)
print("Child Window ID:", Child_Window_Id)

# Example 2: Switch Between Parent and Child Windows

# Switch to child window
driver.switch_to.window(Child_Window_Id)
print(driver.title)

# Switch back to parent window
driver.switch_to.window(Parent_Window_Id)
print(driver.title)

# Example 3: Close a Specific Browser Window Using Title

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(2)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(3)

windowsids = driver.window_handles

for windId in windowsids:
    driver.switch_to.window(windId)

    if driver.title == "OrangeHRM: All in One HR Software for Businesses | OrangeHRM":
        driver.close()

# Switch back to remaining window
driver.switch_to.window(driver.window_handles[0])

# Execution Flow
1- Launch Chrome browser.
2- Open the OrangeHRM login page.
3- Click the OrangeHRM, Inc. link.
4- Open the child browser window.
5- Retrieve all browser window IDs.
6- Switch between browser windows.
7- Check the browser window title.
8- Close the specific matching browser window.
9- Switch back to the parent window.

# Important Points
Every browser window has a unique window ID.
window_handles returns all currently open window IDs.
Selenium initially controls the parent window.
We must switch to another window to interact with it.
close()-    closes only the currently selected window.
quit()-     closes the entire browser session.

# Important Selenium interview questions

driver.window_handles ----> Returns all window IDs

driver.current_window_handle ------> Returns current window ID

driver.switch_to.window(id)------> Switches to a particular window

driver.title ------> Gets current window title

driver.close()------> Closes current window

driver.quit()-----> Closes all browser windows

# One important point to remember: 
1- The for loop checks every open window, switches to it, compares its title, and closes only the window whose title matches.

2- This is a common Selenium interview question under Handling Multiple Browser Windows.