WebDriver Conditional Commands in Selenium
📌 Overview

This project demonstrates the use of Selenium WebDriver conditional commands in Python. These commands help verify the state and properties of web elements before performing actions such as clicking, typing, or selecting options.


📚 Conditional Commands 
# is_displayed()

Checks whether a web element is visible on the webpage.

Example:

search_box = driver.find_element(By.ID, "small-searchterms")
print("Display:", search_box.is_displayed())


Returns: True if the element is displayed; otherwise, False.

# is_enabled()

Checks whether a web element is enabled and available for interaction.

Example:

search_box = driver.find_element(By.ID, "small-searchterms")
print("Enabled:", search_box.is_enabled())


Returns: True if the element is enabled; otherwise, False.

# is_selected()

Checks whether a selectable element, such as a radio button or checkbox, is selected.

Example:

radio_button = driver.find_element(By.ID, "gender-male")
print("Selected:", radio_button.is_selected())


Returns: True if the element is selected; otherwise, False.

🎯 Learning Objectives
Understand Selenium WebDriver conditional commands.

Verify element visibility using is_displayed().

Verify element availability using is_enabled().

Verify checkbox and radio-button selection using is_selected().

Improve the reliability of browser automation scripts.

📝 Notes

Locate the correct element before calling a conditional method.
Use explicit waits (WebDriverWait) when elements load dynamically.
These methods return Boolean values: True or False.
is_selected() is primarily useful for checkboxes, radio buttons, and other selectable elements.


# Links checked and broken links cheched.

# Checkboxes 

# Dropdown 

# Textbox for registration form