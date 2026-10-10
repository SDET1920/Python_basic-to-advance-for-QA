# Relative xpath with text()- Xpath with text()

# For Features link- //a[text()='Features']

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

# Launch website
driver.get("https://www.opencart.com/")
driver.maximize_window()
time.sleep(2)

# Click on Features link.
driver.find_element(By.XPATH,"//a[text()='Features']")
time.sleep(1)

# Print Title name and url
print(driver.title)
print(driver.current_url)

# Close browser
driver.quit()