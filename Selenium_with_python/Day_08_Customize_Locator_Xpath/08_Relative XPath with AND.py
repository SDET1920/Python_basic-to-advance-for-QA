# Relative xpath- Xpath with and

# For Username- //input[@id='input-email' and @name='email']

# For Password- //input[@name='password' and @name='password']

# For login button- //button[@type='submit' and @class='btn']

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
driver.find_element(By.XPATH,"//input[@id='input-email' and @name='email']").send_keys(email)
time.sleep(1)

# Enter the Passowrd
driver.find_element(By.XPATH,"//input[@name='password' and @type='password']").send_keys(password)
time.sleep(1)

# Click on login button # Here contains used becasue Matches the class attribute when it contains that class name in HTML code.
driver.find_element(By.XPATH,"//button[@type='submit' and contains(@class, 'visible-xs-block')]")

# Print Title of website and current url

print("Title:", driver.title)
print("Current Url of Website:", driver.current_url)

# Close browser
driver.close()

