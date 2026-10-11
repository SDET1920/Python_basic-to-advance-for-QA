# Webdriver_Conditional_Command-

# is_display()
# is_enabled()
# is_selected()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Browser
driver= webdriver.Chrome()

# Launch browser
driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
time.sleep(1)

# # Target element
search_box=driver.find_element(By.XPATH,"//input[@id='yesRadio']")
driver.maximize_window()
time.sleep(2)

print("Display:",search_box.is_displayed())
print("Enabled:",search_box.is_enabled())



# is_selected for radio button
radio_button_Partners=driver.find_element(By.XPATH,"//input[@id='yesRadio']")
radio_button_Developer=driver.find_element(By.XPATH,"//input[@id='impressiveRadio']")


print("Default Yes radio button:", radio_button_Partners.is_selected())
print("Default impression radio button:", radio_button_Developer.is_selected())

# After click on YES button
radio_button_Partners.click()

print("You have selected Yes:",radio_button_Partners.is_selected())
print("Not selected:",radio_button_Developer.is_selected())


# Close driver
driver.close()