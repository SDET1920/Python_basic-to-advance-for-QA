# Selenium Locators –
Selenium provides different locator strategies to find elements on a webpage.

# ID
Find an element using its id.

driver.find_element(By.ID, "username")
HTML:

<input id="username">

# NAME
Find an element using its name.

driver.find_element(By.NAME, "email")
HTML:

<input name="email">

# CLASS_NAME
Find an element using its class name.

driver.find_element(By.CLASS_NAME, "login-button")
HTML:

<button class="login-button">Login</button>
Note: Do not use spaces for multiple classes.

# TAG_NAME
Find an element using its HTML tag.

driver.find_element(By.TAG_NAME, "button")
Examples:

driver.find_element(By.TAG_NAME, "input")
driver.find_element(By.TAG_NAME, "h1")
driver.find_element(By.TAG_NAME, "a")

# LINK_TEXT
Find a link using its complete visible text.

driver.find_element(By.LINK_TEXT, "Download")
HTML:

<a href="/download">Download</a>

# PARTIALLINKTEXT
Find a link using part of its visible text.

driver.find_element(By.PARTIAL_LINK_TEXT, "Down")
HTML:

<a href="/download">Download OpenCart</a>

# Locator Summary

Locator	Example
ID	                By.ID, "username"
NAME	            By.NAME, "email"
CLASS_NAME	        By.CLASS_NAME, "login"
TAG_NAME	        By.TAG_NAME, "button"
LINK_TEXT	        By.LINK_TEXT, "Download"
PARTIAL_LINK_TEXT	By.PARTIAL_LINK_TEXT, "Down"