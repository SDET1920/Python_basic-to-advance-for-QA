# Approach 2

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
windowsids=driver.window_handles

for windId in windowsids:
    driver.switch_to.window(windId)
    print(driver.title)


# Close browser
driver.quit()