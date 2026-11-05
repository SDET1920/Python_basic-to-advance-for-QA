# Date Picker--- Normal Approach


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome browser
driver=webdriver.Chrome()

# Launch browser
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(2)

# Switch to frame
driver.switch_to.frame(0)

# Pick the date.  # Date format- 11/30/2026   MM/DD/YYYY
Date=driver.find_element(By.XPATH,"//input[@id='datepicker']")
Date.send_keys("11/30/2026")

# Used get_attribute to print expected value.
date_value = Date.get_attribute("value")
print("Month/Date/Year:", date_value)
time.sleep(5)