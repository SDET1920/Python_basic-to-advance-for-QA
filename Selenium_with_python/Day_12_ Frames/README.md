# Frames Handling in Selenium with Python
📌 Introduction
In Selenium WebDriver, frames (iframes) are used to display one HTML page inside another HTML page.

To interact with elements inside a frame, we must first switch the WebDriver focus to that frame.

Selenium provides different methods to handle frames using Python.


# Types of Frames
There are three common ways to identify and switch to frames:

Using Frame Name or ID
Using Frame Index
Using WebElement
🔹 Important Methods for Frame Handling

# Method	Description
driver.switch_to.frame()	Switches to a specific frame
driver.switch_to.parent_frame()	Switches to the parent frame
driver.switch_to.default_content()	Switches back to the main webpage

# Practical Example: Handling Multiple Frames
Practice Website:
https://www.hyrtutorials.com/p/frames-practice.html

# Python Code

python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver = webdriver.Chrome()

# Launch browser
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")

# Maximize window
driver.maximize_window()

# Time sleep
time.sleep(2)

# Frame 1
driver.switch_to.frame("frm1")
driver.find_element(By.ID, "Home").click()
driver.switch_to.default_content()

# Frame 2
driver.switch_to.frame("frm2")
driver.find_element(
    By.XPATH,
    "//b[normalize-space()='First Name']"
).send_keys("Shiv k")
driver.switch_to.default_content()

# Frame 3
driver.switch_to.frame("frm3")
driver.find_element(By.LINK_TEXT, "Buy me a coffee").click()

# Close driver
driver.quit()
🔍 Explanation of the Code
1. Launch Browser

python
driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
Launches Chrome browser and opens the practice website.

2. Switch to Frame 1

python
driver.switch_to.frame("frm1")
driver.find_element(By.ID, "Home").click()
Switches to the first frame using its ID.
Finds the Home element and clicks it.
3. Switch Back to Main Page

python
driver.switch_to.default_content()
Switches the WebDriver focus from the frame back to the main webpage.

4. Switch to Frame 2

python
driver.switch_to.frame("frm2")
driver.find_element(
    By.XPATH,
    "//b[normalize-space()='First Name']"
).send_keys("Shiv k")
Switches to the second frame and enters text into the located input element.

5. Switch to Frame 3

python
driver.switch_to.frame("frm3")
driver.find_element(By.LINK_TEXT, "Buy me a coffee").click()
Switches to the third frame and clicks the specified link.

6. Close Browser

python
driver.quit()
Closes all browser windows and ends the WebDriver session.

📖 Different Ways to Switch Frames
1. Using Frame Name or ID

python
driver.switch_to.frame("frm1")
2. Using Frame Index

python
driver.switch_to.frame(0)
3. Using WebElement

python
frame = driver.find_element(By.ID, "frm1")
driver.switch_to.frame(frame)

⚠️ Important Notes
Always switch to a frame before interacting with its elements.
Use default_content() to return to the main webpage.
Use parent_frame() to move one level up in nested frames.
Frame index starts from 0.
Use explicit waits instead of time.sleep() for more reliable automation.
If an element is not found, verify that you are in the correct frame.