# Locator-- Partial link text()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

# Open website

driver.get("https://www.opencart.com")
driver.maximize_window()
time.sleep(2)


# Capture Partiallintext()

element= driver.find_element(By.PARTIAL_LINK_TEXT,"Download")

time.sleep(2)

print(driver.title)


driver.close()