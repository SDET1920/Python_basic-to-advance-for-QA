# Alerts and Popups Handling in Selenium with Python
📌 Introduction
In Selenium WebDriver, alerts and popups are used to display messages, request user confirmation, or collect input from users.

Selenium provides built-in methods to handle JavaScript alerts, confirmation boxes, prompt boxes, and multiple browser windows.

This repository explains how to handle different types of alerts and popups using Python and Selenium WebDriver.

# Types of Alerts in Selenium
There are three main types of JavaScript alerts:

# Simple Alert
A simple alert displays a message with an OK button.

Handling Simple Alert:


python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element("xpath", "//button[text()='Click for JS Alert']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()

driver.quit()

2. Confirmation Alert
A confirmation alert displays a message with two options:

OK – Accepts the alert.
Cancel – Dismisses the alert.
Accept Confirmation Alert:


python
driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()
Dismiss Confirmation Alert:


python
driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()

alert = driver.switch_to.alert

alert.dismiss()

# Prompt Alert
A prompt alert allows users to enter text.

Handling Prompt Alert:


python
driver.find_element("xpath", "//button[text()='Click for JS Prompt']").click()

alert = driver.switch_to.alert

print(alert.text)

alert.send_keys("Hello Selenium")

alert.accept()

# Handling Browser Popups / Multiple Windows
Sometimes clicking a link or button opens a new browser window or tab.

Selenium provides the following methods:

driver.current_window_handle – Returns the current window ID.
driver.window_handles – Returns all open window IDs.
driver.switch_to.window() – Switches to another window.
driver.close() – Closes the current window.
driver.quit() – Closes all browser windows.

# Important Selenium Methods

Method	Description
switch_to.alert	Switches to the alert
alert.accept()	Clicks OK
alert.dismiss()	Clicks Cancel
alert.text	Gets alert message
alert.send_keys()	Enters text in prompt
current_window_handle	Gets current window ID
window_handles	Gets all window IDs
switch_to.window()	Switches browser window
close()	Closes current window
quit()	Closes entire browser session