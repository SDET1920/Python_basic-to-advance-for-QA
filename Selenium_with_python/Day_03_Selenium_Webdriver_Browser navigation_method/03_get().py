# Webdriver methods- ebDriver has many useful methods for controlling the browser.
# Here are the most important ones you should learn first.

# 1- get()- Opens a URL.
# 2- back()- Goes back to the previous page.
# 3- forward()- Moves forward in browser history.
# 4- refresh()- Refreshes the current page.
# 5- close()- Closes the current browser window/tab.
# 6- quit()- Closes the entire browser session.

#Difference: close() and quit()

#close() → closes current window/tab
#quit()  → closes all windows and ends WebDriver session


# Example 1- get()- Opens a URL.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)


