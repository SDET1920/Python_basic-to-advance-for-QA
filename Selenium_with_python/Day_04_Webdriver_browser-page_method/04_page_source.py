# 3- page_source- Gets the HTML source of the current page.


from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

print(driver.page_source)