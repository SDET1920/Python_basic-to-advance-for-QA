# Xpath_Axes- Self

# Self-- //a[contains(text(),'VTM')]/self::a

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

# Launch website
driver.get("https://money.rediff.com/gainers/bse/daily/groupall")
driver.maximize_window()
time.sleep(2)

# Click on self locator
# text_message= driver.find_element(By.XPATH,"//a[contains(text(),'VTM')]/self::a").text
# print("Captureing text message of Self locator:", text_message)
# time.sleep(1)

# Parent locator
# text_message= driver.find_element(By.XPATH,"//a[contains(text(),'VTM')]/parent::td").text
# print("Captureing text message of parent locator:", text_message)
# time.sleep(1)

# Child locator
# Text_Count= driver.find_elements(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr/child::td")
# print("Print len of child:",len(Text_Count))
# time.sleep(1)

# Ancestor locator
# Text_Count= driver.find_element(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr").text
# print(Text_Count)
# time.sleep(1)

# Descendant locator
# Text_Count= driver.find_elements(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr/descendant::*")
# print(len(Text_Count))
# time.sleep(1)

# Following locator
# Text_Count= driver.find_elements(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr/following::*")
# print("Total count of following:", len(Text_Count))
# time.sleep(1)

# Following-sibiling locator
# Count= driver.find_elements(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr/following-sibling::*")
# print("Total count of following-sibling:", len(Count))
# time.sleep(1)

# Preceding locator
# Count= driver.find_elements(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr/preceding::*")
# print("Total count of following-sibling:", len(Count))
# time.sleep(1)

# Preceding-sibling locator
Count= driver.find_elements(By.XPATH,"//a[contains(text(),'VTM')]/ancestor::tr/preceding-sibling::*")
print("Total count of Preceding-sibling:", len(Count))
time.sleep(1)


# Print Title name and url
print("Title of website:", driver.title)
print("Current title of website:", driver.current_url)

# Close browser
driver.quit()