# Date Picker--- Loop Approach.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome browser
driver=webdriver.Chrome()

# Launch browser
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(2)

# Switch to frame-- The date picker is inside an iframe
# frame(0) means switch to the first iframe.
# After switching, Selenium can access the date picker.
driver.switch_to.frame(0)

# Pick the date.  # Date format- 11/30/2026   MM/DD/YYYY
# Declare date, month and year
year="2021"
month="January"
date="11"

# Open Date Picker......
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
time.sleep(2)
#  Navigate to the required month and year
while True: #The loop continues until the required month and year are found and the break statement executes.
    Mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text      #Month pick
    Yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text        #Year pick

    if Mon==month and Yr==year:
        break
    else:
        #driver.find_element(By.XPATH,"//a[@title='Next']").click() # For forward button
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()  # For Privious button
time.sleep(2)
# Pick Date from datepicker
dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date_Element in dates:
    if date_Element.text==date:
        date_Element.click()
        break

time.sleep(2)


# Close browser
driver.quit()





