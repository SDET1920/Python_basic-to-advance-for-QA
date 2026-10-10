## # Customer locators

# Tag and attribute-

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

# Launch url..
driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(1)

# Attribute locator
driver.find_element(By.CSS_SELECTOR,"[name='email']").send_keys("sshivamchauhan@gmail.com")
time.sleep(1)

# Or Tag and Atrribute.
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("Shiv@kishor")
time.sleep(1)

# click on login button
driver.find_element(By.CLASS_NAME,"btn").click()

# Will check if logged in successfully the title should be print
print(driver.title)

# close driver
driver.close()

