# Locator- TAG_NAME()- used fro login button.

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

# Open website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# Maxmize broswer
driver.maximize_window()
time.sleep(2)

# Name locator for user name- Enter username
driver.find_element(By.NAME,"username").send_keys("Admin")

# Name locator for password- Enter password
driver.find_element(By.NAME,"password").send_keys("admin123")

# Click on login button
driver.find_element(By.TAG_NAME,"button").click()

# Verify title
print(driver.title)

time.sleep(2)
driver.close()


