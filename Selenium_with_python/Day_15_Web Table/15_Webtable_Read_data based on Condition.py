# Webtable- Read data based on condition

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
print(Capture_Text_data)

# Read data based on condition(List books name whose author is Mukesh, BookName and Price)
for r in range(2,Num_of_rows+1):
    authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookName,"         ",authorName,"       ",price)

# close driver
driver.close()