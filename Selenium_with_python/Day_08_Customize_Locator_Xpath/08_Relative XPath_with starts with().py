# Relative xpath with contains()- Xpath with start with path()

# For Username- //input[starts-with(@id,'input-email')]

# For Password- //input[starts-with(@id,'input-password')]

# For login button- //input[starts-with(@id,'input-password')]

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
driver.find_element(By.XPATH,"//input[starts-with(@id,'input-email')]").send_keys(email)
time.sleep(1)

# Enter the Passowrd
driver.find_element(By.XPATH,"//input[starts-with(@id,'input-password')]").send_keys(password)
time.sleep(1)

# Click on login button // herw was two button so i given the indexing [1].
driver.find_element(By.XPATH,"//button[starts-with(@type,'submit')][1]")

# Print Title of website and current url

print("Title:", driver.title)
print("Current Url of Website:", driver.current_url)

# Close browser
driver.close()
