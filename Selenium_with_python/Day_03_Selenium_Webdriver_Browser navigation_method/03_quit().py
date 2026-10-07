# Example 6- quit()- Closes the entire browser session.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)

driver.quit()