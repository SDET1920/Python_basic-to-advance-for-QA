# Frames

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")

# Maxmize window
driver.maximize_window()
# time sleep
time.sleep(2)

# Frame 1
driver.switch_to.frame("frm1")
time.sleep(2)

course =Select(driver.find_element(By.ID, "course"))
course.select_by_visible_text("Java")

driver.switch_to.default_content()
time.sleep(2)

# Frame 2
driver.switch_to.frame("frm2")

driver.find_element(By.ID, "firstName").send_keys("Shiv k")

driver.switch_to.default_content()
time.sleep(2)

# Frame 3
driver.switch_to.frame("frm3")

driver.find_element(By.LINK_TEXT, "Buy me a coffee").click()

driver.switch_to.default_content()

time.sleep(2)
driver.quit()