# 1- minimize_window()-  driver.minimize_window()


from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.minimize_window()
