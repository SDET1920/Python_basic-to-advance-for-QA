# Browser Window- Simple method

# Approach 1

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Select browser
driver=webdriver.Chrome()

# Launch browser
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)

# Window Id of single browser window
#windowid=driver.current_window_handle   # Return WindowID of single browser window.
#print(windowid)   #WindowID= BD74D6588EAA043326ED2636D6A4C5D2

# Window Id's of multiple browser window
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsids=driver.window_handles

# capture Parent and child window id's and store it
Parent_Window_Id= windowsids[0]  #Parent_Window_Id= 3A5DC0F7AA31E4B27991EF95DA0FCC48
Child_Window_Id= windowsids[1]   #Child_Window_Id=  CC0080CE79A1AE405C7A726E482C749B

print(Parent_Window_Id, Child_Window_Id)

# Print Child window title for verify.
driver.switch_to.window(Child_Window_Id)
print("Title of the child window:",driver.title)

# Print Parent window title for verify
driver.switch_to.window(Parent_Window_Id)
print("Title of the parent window:",driver.title)

time.sleep(1)

# Close browser
driver.quit()