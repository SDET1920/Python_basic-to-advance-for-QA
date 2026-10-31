# Inner frame

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(2)

# Click on button on frame

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(2)

# Outer Frame....
outerFrame= driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)
time.sleep(2)

# Inner Frame..
innerFrame=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)
time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Welcome")
time.sleep(2)

#driver.switch_to.parent_frame()  #directly switch to parent frame(outerframe)

# close browser

driver.quit()