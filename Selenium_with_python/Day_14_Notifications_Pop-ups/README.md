# Handling Notification Pop-ups in Selenium with Python
1. Introduction

In Selenium automation, notification pop-ups are browser-level messages displayed by websites to request permission to show notifications.

Using Selenium with Python, we can allow, block, or manage browser notification permissions through ChromeOptions and Chrome preferences.


# 2 Allow Browser Notifications

To allow website notifications, set the Chrome notification preference to 1.

Python Code
python
from selenium import webdriver

options = webdriver.ChromeOptions()

prefs = {
    "profile.default_content_setting_values.notifications": 1
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://example.com")

print("Browser notifications are allowed")

driver.quit()

# 2 Block Browser Notifications

To block website notifications, set the notification preference to 2.

Python Code
python
from selenium import webdriver

options = webdriver.ChromeOptions()

prefs = {
    "profile.default_content_setting_values.notifications": 2
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get("https://example.com")

print("Browser notifications are blocked")

driver.quit()

# 3 Disable Notifications Using ChromeOptions

We can also disable notification pop-ups using the Chrome argument:

python
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)

driver.get("https://example.com")

driver.quit()

# 4 Notification Permission Values

Value	    Description
0	        Default browser setting
1	        Allow notifications
2	        Block notifications

# Difference Between Browser Notifications and JavaScript Alerts

Browser Notifications	                     JavaScript Alerts
Browser-level permission pop-ups	          JavaScript-generated dialog boxes
Managed using ChromeOptions	                  Managed using switch_to.alert
Cannot be handled using switch_to.alert	      Can be handled using switch_to.alert

# Handling JavaScript Alerts
python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

print(alert.text)

alert.accept()

driver.quit()

# Important Interview Questions

Q1. How do you handle notification pop-ups in Selenium?

We can handle browser notifications using ChromeOptions and Chrome preferences.

Q2. How do you block notifications in Chrome?

By setting:

python
"profile.default_content_setting_values.notifications": 2


Q3. How do you allow notifications in Chrome?

By setting:

python
"profile.default_content_setting_values.notifications": 1


Q4. Can we handle browser notifications using switch_to.alert?

No. Browser notifications are different from JavaScript alerts. We manage browser notification permissions through browser options.

Q5. What is the difference between accept() and dismiss()?

accept() clicks OK on a JavaScript alert or accepts a confirmation.
dismiss() cancels or rejects a confirmation dialog.

# Conclusion

Selenium with Python provides ChromeOptions and browser preferences to manage notification permissions.

This approach is useful in automation testing because unwanted browser notifications can interrupt test execution.