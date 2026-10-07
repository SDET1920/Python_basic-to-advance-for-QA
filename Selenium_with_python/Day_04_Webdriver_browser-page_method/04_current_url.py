# 2- current_url- Gets the current URL.

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

print(driver.current_url)
