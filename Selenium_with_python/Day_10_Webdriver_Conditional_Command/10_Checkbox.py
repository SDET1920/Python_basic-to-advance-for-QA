# Check box- Example for registration page


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)

# 1- Capture checkbox locator and calculated now of weekdays.

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print("Print Weekdays count:", len(checkboxes))
time.sleep(2)

# 1= Approach 1---All checkboxes will be select.
# for checkbox in checkboxes:
#     checkbox.click()


# 2- Approach 2-- All Checkboxes will be select
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# 3- Approach 3- select multiple checkboxes by choice.

# for checkbox in checkboxes:
#     weekname= checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#        checkbox.click()


# 4- Approach 4- Select last 2 checkboxes
# Logic- range(5,7) -->6,7
# Logic- totalnumberofelements-2=starting index

# for i in range(len(checkboxes)-2,len(checkboxes)):
#      checkboxes[i].click()

# 5- Approach 5- Select first 2 checkboxes using range.
# for i in range(0, 2):
#      checkboxes[i].click()

# 6- Approach 6- Select first 2 checkboxes using range.

# for i in range(2):
#      checkboxes[i].click()


# 7- Approach 7- Select first 2 checkboxes using condition.
# for i in range(len(checkboxes)):
#      if i<2:
#         checkboxes[i].click()

# 8- Approach 8- clearing all the check boxes

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


# close browser
driver.quit()