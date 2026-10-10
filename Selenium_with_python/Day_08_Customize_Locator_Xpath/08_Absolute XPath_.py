# Absolute xpath-- it's full xpath which can we write from Root to node element.

#Example UserName- /html/body/div[2]/div[2]/div/div[1]/form/div[1]/input
#Example Password- /html/body/div[2]/div[2]/div/div[1]/form/div[2]/input
#Example Login- /html/body/div[2]/div[2]/div/div[1]/form/div[3]/div[1]/button[1]

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Credential import email, password

# Launch Chrome
driver= webdriver.Chrome()

# Open website.
driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(1)

# Enter username
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/form/div[1]/input").send_keys(email)
time.sleep(1)

# Enter Password
driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/form/div[2]/input").send_keys(password)
time.sleep(1)

# Click on login button

driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[1]/form/div[3]/div[1]/button[1]").click()
time.sleep(1)
# Print Title and current url

print(driver.title)

# Quit browser

driver.quit()