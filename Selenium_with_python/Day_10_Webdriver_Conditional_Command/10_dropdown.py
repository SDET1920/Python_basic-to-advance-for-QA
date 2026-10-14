# Example- Drop down

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# Select drop down in website.
dropdown=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
time.sleep(2)

# Select dropdown by visible text
dropdown.select_by_visible_text("India")  #Result- India


# Select dropdown by Value
dropdown.select_by_value("china")  #Result- China

# Select dropdown by Index value
dropdown.select_by_index(8)  #Result- Brazil

# Capture all the options and print all.
Capture_all=dropdown.options
print("Capture all options and print:", len(Capture_all))

for all in Capture_all:
    print(all.text)            # Print all Country's name.


# Select option from dropdown without using built-in method

for all in Capture_all:
      if all.text=="India":
          all.click()
          break

# Diffrent approach to capture xpath for dropdown
Total_Count=driver.find_elements(By.XPATH,"//select[@id='country']/option")
print("Toto count of Countary in dropdown:",len(Total_Count))

time.sleep(5)
# Close the browser
driver.quit()