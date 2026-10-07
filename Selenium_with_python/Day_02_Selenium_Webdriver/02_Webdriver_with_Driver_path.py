# Chrome with driver path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Drivers/chromedriver_win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")



# Firefox with driver path

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service("C:/Drivers/geckodriver-v0.37.1-win64/geckodriver.exe")
driver = webdriver.Firefox(service=service)

driver.get("https://www.google.com")

# Edge for driver path.

from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service("C:/Drivers/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.get("https://www.google.com")

