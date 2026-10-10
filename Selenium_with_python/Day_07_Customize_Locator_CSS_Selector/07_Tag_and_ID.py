# Customer locators

# CSS locators- 1- Tag and ID-- #id

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()

# Open website

driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(2)

# Enter user name
driver.find_element(By.CSS_SELECTOR,"#input-email").send_keys("sshivamchauhan@gmail.com")
time.sleep(1)

# Enter passowrd
driver.find_element(By.CSS_SELECTOR,"#input-password").send_keys("Shiv@kishor")
time.sleep(1)
# Click on login button.

driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(1)
# Print title of website
print(driver.title)

driver.close()

