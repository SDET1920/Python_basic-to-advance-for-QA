# Webtable- Simple approach

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome browser
driver=webdriver.Chrome()

# Launch browser
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(1)

# Count num of rows from webtable
Num_of_rows= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))

# Count num of columns from webtable
Num_of_columns= len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))

# Print both Num of rows and columns
print("Total Number of Rows:",Num_of_rows)
print("Total Number of Columns:", Num_of_columns)

# Capture data from sepcific row and column.
Capture_Text_data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody//tr[5]/td[1]").text

# Print capture text data
print(Capture_Text_data)

# Close browser
driver.quit()