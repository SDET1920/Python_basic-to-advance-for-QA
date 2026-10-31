# Alerts- Popups-

# 1- click for js alert.

# test steps-- click on js alert>Switch to alert > print alert text>

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(2)

# # Click the JS Alert button
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()

time.sleep(2)
# Switch to the JavaScript alert
myalert=driver.switch_to.alert

#Print alert text
print(myalert.text)
time.sleep(2)

# Accept the alert
myalert.accept()

# close browser
driver.quit()