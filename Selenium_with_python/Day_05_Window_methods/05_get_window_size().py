# get_window_size()---

# size = driver.get_window_size()
# print(size)

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

size= driver.get_window_size()
print(size)
