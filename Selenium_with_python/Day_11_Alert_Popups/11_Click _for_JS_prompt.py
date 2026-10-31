# 3 Click for JS_prompt()

# test steps-- click on js alert> Switch to alert> send text in JS and print alert text> Accept or dismiss

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(2)

# Capture locator and click on JS Alert button
alert=driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()


# Switch to the JavaScript alert
myalert=driver.switch_to.alert
time.sleep(2)

# Print alert text
print(myalert.text)

# Send text in alert
myalert.send_keys("I am a JS prompt")
time.sleep(2)

# Accept alert
#myalert.accept()

# Dismiss alert
myalert.dismiss()

# close driver
driver.quit()

