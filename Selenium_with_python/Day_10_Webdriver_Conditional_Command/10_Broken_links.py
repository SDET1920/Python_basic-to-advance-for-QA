# Broke links capture in website.

import requests as requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

# Open url
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# Target links in website.
all_links=driver.find_elements(By.TAG_NAME,"a")
count=0
print("Total links:", len(all_links))

for links in all_links:
    url=(links.get_attribute("href"))
    try:
     res=requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print("It's Broken Links:", url)
        count += 1
    else:
        print("It's Valid Links:", url)

print("Total number of broken links:", count)

# Driver close
driver.quit()