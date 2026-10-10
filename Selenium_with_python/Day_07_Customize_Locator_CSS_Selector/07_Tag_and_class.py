# Customer locators

# CSS locators- 2- Tag and class-   .class

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()

# Open website

driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(2)

# Enter Username
driver.find_elements(By.CSS_SELECTOR,".form-control")[0].send_keys("sshivamchauhan@gmail.com")


time.sleep(1)

# Enter Passowrd
driver.find_elements(By.CSS_SELECTOR,".form-control")[1].send_keys("Shiv@kishor")

time.sleep(1)
# Click on login button.

driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(1)
# Print title of website
print(driver.title)
