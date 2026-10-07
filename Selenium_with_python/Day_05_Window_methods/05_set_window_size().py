# 1- set_window_size()-  driver.set_window_size(1200, 800)


from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

driver.set_window_size(1200,800)
time.sleep(2)