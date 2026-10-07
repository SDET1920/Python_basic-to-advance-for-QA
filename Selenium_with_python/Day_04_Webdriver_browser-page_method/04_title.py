# Webdriver method- Get information about the browser/page

# 1- title- Gets the current page title.
# 2- current_url- Gets the current URL.
# 3- page_source- Gets the HTML source of the current page.



# 1- title- Gets the current page title.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

print(driver.title)
