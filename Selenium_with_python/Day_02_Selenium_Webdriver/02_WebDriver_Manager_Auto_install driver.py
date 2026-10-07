# Webdriver manager-Python library that automatically downloads and manages the browser driver
# (such as ChromeDriver) needed by Selenium.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# or below code also can use as per simlicity

# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install())
# )

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)