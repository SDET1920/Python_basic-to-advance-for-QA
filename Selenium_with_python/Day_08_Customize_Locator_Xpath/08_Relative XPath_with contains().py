# Relative xpath with contains()- Xpath with contains()

# For Username- //input[contains(@name,'em')]

# For Password- //input[contains(@id,'input-password')]

# For login button- //button[contains(@type,'submit')]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Credential import email, password

driver=webdriver.Chrome()

# Launch website
driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(2)

# Enter the UserName
driver.find_element(By.XPATH,"//input[contains(@name,'em')]").send_keys(email)
time.sleep(1)

# Enter the Passowrd
driver.find_element(By.XPATH,"//input[contains(@id,'input-password')]").send_keys(password)
time.sleep(1)

# Click on login button # Here contains used becasue Matches the class attribute when it contains that class name in HTML code.
driver.find_element(By.XPATH,"//button[contains(@type,'submit')]")

# Print Title of website and current url

print("Title:", driver.title)
print("Current Url of Website:", driver.current_url)

# Close browser
driver.close()
