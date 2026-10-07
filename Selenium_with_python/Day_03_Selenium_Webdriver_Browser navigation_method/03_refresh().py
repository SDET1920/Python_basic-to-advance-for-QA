
# Example 4- refresh()- Refreshes the current page.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

driver.refresh()
time.sleep(1)