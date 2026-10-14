# Links test- All links, included broken link.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(1)

# Capture links count
links=driver.find_elements(By.XPATH,"//a")
print("ALl links present:", len(links))

## Capture all links text-name along with url.

for link in links:
    print(link.text, link.get_attribute("href"))

# close browser
driver.quit()