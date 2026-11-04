# Webtable- Read data based on condition


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome browser
driver = webdriver.Chrome()

# Launch browser
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

# User name
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
time.sleep(1)

# User Password
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")

# Click on login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Admin -> User Management -> Users
driver.find_element(By.XPATH, "//span[text()='Admin']").click()
time.sleep(5)

# Table data capture
Num_of_Rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']"))
print("Total Num of Rows:", Num_of_Rows)

# Capture number of columns
Num_of_Columns = len(driver.find_elements(By.XPATH,"(//div[@class='oxd-table-body']//div[@role='row'])[1]/div"))
print("Total Num of Columns:", Num_of_Columns)

# Verify the Title of website
print("Website Title:", driver.title)

# Approach 1 - Simple method
enabled_count = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[text()='Enabled']"))
disabled_count = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[text()='Disabled']"))

print("Enabled Users:", enabled_count)
print("Disabled Users:", disabled_count)
time.sleep(5)

# Approach 2 - Using for loop
count = 0
status_list = driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']//div[@role='row']/div[5]")
for status in status_list:

    if status.text == "Enabled":     #.text here used else we can use in print(status.text)
        count = count + 1

print("Total Number of users:", Num_of_Rows)
print("Number of enabled users:", count)
print("Number of disabled users:", Num_of_Rows-count)     #This logic use to find Disable users or we can use if else.

# Close browser
driver.quit()


# Approach 3-- Using for loop and count (it's having some xpath issues in webtable)
count=0
for r in range(1,Num_of_Rows+1):
    status=driver.find_element(By.XPATH,"//div[@class='oxd-table-body']//div[@role='row']["+str(r)+"]/div[5]").text
    if status=="Enabled":
        count=count+1

print("Total Number of users:",Num_of_Rows)
print("Number of enabled users:",count)
print("Number of disabled users:",(Num_of_Rows-count))

# Approach 4--- if and else condition used to find "Enable" and "Disable" users.
enabled = 0
disabled = 0

status_list = driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']//div[@role='row']/div[5]")

for status in status_list:

    if status.text == "Enabled":
        enabled += 1

    elif status.text == "Disabled":
        disabled += 1

print("Enabled Users:", enabled)
print("Disabled Users:", disabled)
