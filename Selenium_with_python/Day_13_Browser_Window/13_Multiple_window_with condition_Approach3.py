# Approach 3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Select browser
driver=webdriver.Chrome()

# Launch browser
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# Window Id's of multiple browser window
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(1)

# Get all windows id's
windowsids=driver.window_handles

# Close specific browser windows   1 2 3
for windId in windowsids:
    driver.switch_to.window(windId)
    if driver.title=="OrangeHRM: All in One HR Software for Businesses | OrangeHRM":
        driver.close()

