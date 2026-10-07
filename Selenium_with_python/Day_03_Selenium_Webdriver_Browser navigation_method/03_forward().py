# Example 3- forward()- Moves forward in browser history.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(1)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)

driver.back()     # Go back to google.com
time.sleep(1)

driver.forward()  # Go forward to Orangehrms
time.sleep(1)

