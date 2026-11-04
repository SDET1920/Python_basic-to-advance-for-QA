# Webtable- Read row and column data.....

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

# Read Row and column data...
for r in range(2,Num_of_rows+1):        # r and c are integers.
    for c in range(1,Num_of_columns+1): # XPath is a string / We use str() to convert integers into strings.
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end='           ')  # print(data, end=' ') → Prints column data on the same line.
    print()                           # print() → Moves to the next row/data from the next row gets printed on a new line.

# Close browser
driver.close()

