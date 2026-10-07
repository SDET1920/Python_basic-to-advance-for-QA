# Locator- Class_NAME()- alwasy use short name from class name othere wise it will give #Compound class names are not allowed

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

# Open Opercart website
driver.get("https://www.opencart.com/index.php?route=account/login")

# maxmize window
driver.maximize_window()
time.sleep(1)

# Enter Email
driver.find_element(By.ID,"input-email").send_keys("ssshivamchauhan@gmail.com")
time.sleep(1)
# Enter password
driver.find_element(By.ID,"input-password").send_keys("Shiv@kishor")
time.sleep(1)

# Click login
driver.find_element(By.CLASS_NAME,"btn").click()


print(driver.title)

driver.close()