
# Example 5- close()- Closes the current browser window/tab.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)

driver.close()     #Closes the current browser window/tab.
