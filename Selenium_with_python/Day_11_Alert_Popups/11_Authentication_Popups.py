# Alerts- Popups-

# 4- Authentication_Popups()----

# test steps-- Launch url> authentication required (user id and password)> click on sign in or Cancel

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser- with real website
#driver.get("http://the-internet.herokuapp.com/basic_auth")

# By pass the authentication using bypass logic....
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(2)

# I used Validation the (body) tag will capture overall body of this page, where i printed the text and message.

message = driver.find_element(By.TAG_NAME, "body").text
print(message)

# Validate the message using if-else
if "Congratulations!" in message:
    print("Test Passed: Authentication successful")
else:
    print("Test Failed: Authentication unsuccessful")