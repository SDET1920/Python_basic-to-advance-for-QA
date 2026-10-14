# Text box- Example for registration page


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

# User name
driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("Shiv k")
time.sleep(1)

# Email id
driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("Shiv@gmail.com")
time.sleep(1)

# Current address
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Sec:0, City: Delhi, Pin:20000")
time.sleep(1)

# Parmanet address
driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Sec:123, City:Noida, Pin:20001")
time.sleep(1)

# print title and current url
print(driver.title, driver.current_url)
# close browser

driver.quit()