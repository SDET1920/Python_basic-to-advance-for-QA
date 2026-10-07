# 1- fullscreen_window()-  driver.fullscreen_window()

from selenium import webdriver
import time

driver= webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)

driver.fullscreen_window()
time.sleep(2)
