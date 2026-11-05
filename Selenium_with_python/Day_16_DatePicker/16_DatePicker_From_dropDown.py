# Date Picker--- From Drop Down Calender.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Chrome browser
driver=webdriver.Chrome()

# Launch browser
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(2)

# Date of Birth--Open Date picker..
driver.find_element(By.XPATH,"//input[@id='dob']").click()

# Select Month-----
datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Oct")

# Select Year-----
datepicker_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("1994")

# All dates---
alldates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in alldates:
    if date.text=="18":
        date.click()
        print(date.text)
        break

