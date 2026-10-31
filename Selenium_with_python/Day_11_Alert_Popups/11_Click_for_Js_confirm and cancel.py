# Alerts- Popups-

# 2- click for js confirm and cancel

# test steps-- click on js alert>Switch to alert >Accept or dismiss> print alert text

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
driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
time.sleep(2)

# Switch to the JavaScript alert
myalert=driver.switch_to.alert

# Print alert text
print(myalert.text)

time.sleep(2)

# Accept the alert
myalert.accept()

# Capture result text from webpage- This code only for verify the text with accept()
result= driver.find_element(By.XPATH,"//p[@id='result']").text

if result == "You clicked: Ok":
    print("Test Passed: Result text is correct")
else:
    print("Test Failed: Result text is incorrect")


# Dismiss the alert
# myalert.dismiss()
#
# # Capture result text from webpage- This code only for verify the text with dismiss()
# result= driver.find_element(By.XPATH,"//p[@id='result']").text
#
# if result == "You clicked: Cancel":
#     print("Test Passed: Result text is correct")
# else:
#     print("Test Failed: Result text is incorrect")


# Close browser
driver.quit()