#Note- 

webdriver.chrome(executable_path=...)

In newer versions of Selenium, executable_path is no longer supported this way. Use Service instead.

# Selenium 4.50 latest version

Yes. With modern Selenium 4, you generally do not need to manually download ChromeDriver, GeckoDriver, or EdgeDriver.

Selenium Manager automatically finds/downloads the appropriate browser driver.

#Example 1- Automatic approach.
#Chrome
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

#Firefox
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.google.com")

#Microsoft Edge
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.google.com")


#Example 2- Manual approach for best company projects.

# Chrome with driver path 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Drivers/chromedriver_win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# Type of selenium webdriver-

Yes. In Selenium, there are several types of WebDriver implementations, mainly corresponding to different browsers.

Common WebDrivers---
Browser	                 Selenium code
Chrome	                 webdriver.Chrome()
Firefox	                 webdriver.Firefox()
Edge	                 webdriver.Edge()
Safari	                 webdriver.Safari()
Internet Explorer	     webdriver.Ie() (obsolete)