## # Customer locators

# Tag, Class and attribute-


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# The test casea is running in 3 browsers in same time.
driver= webdriver.Chrome()
driver= webdriver.Firefox()
driver= webdriver.Edge()

# Open Url

driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(1)

# Enter user name and capture the locator

driver.find_element(By.CSS_SELECTOR,"input.form-control[placeholder='Email']").send_keys("sshivamchauhan@gmail.com")
time.sleep(2)
# Enter password and cpature the locator

driver.find_element(By.CSS_SELECTOR,"input.form-control[placeholder='Password']").send_keys("Shiv@kishor")
time.sleep(2)

# Click on login button

driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

# print one validation

print(driver.current_url)

driver.quit()