from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#options = webdriver.ChromeOptions()         #Both can we use
options = Options()                          # Both can we use
prefs = {
    "profile.default_content_setting_values.notifications": 1
}

options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

# Launch browser
driver.get("https://www.pushengage.com/?utm_source=chatgpt.com")
driver.maximize_window()
time.sleep(1)

print("Website opened successfully")

# Close browser
driver.quit()
