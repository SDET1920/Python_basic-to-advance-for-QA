# Locator-- linktext()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()


# Opne website

driver.get("https://www.opencart.com")
driver.maximize_window()
time.sleep(2)

# Capture linktext- Features and click on the link

driver.find_element(By.LINK_TEXT,"Features").click()
time.sleep(2)

driver.close()





