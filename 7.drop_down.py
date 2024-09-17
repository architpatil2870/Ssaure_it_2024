from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
# import time

# from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Specify the path to the chromedriver executable
service = Service(executable_path=r"C:\Users\archi\Downloads\chromedriver-win32\chromedriver.exe")

# Initialize the WebDriver with service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to a URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# select by visible text
# select by value
# select by index


# Locate the dropdown element by its id
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))

# Select an option by visible text
dropdown.select_by_visible_text("Option1")

# Select an option by index
# dropdown.select_by_index(2)
#
# # Select an option by value
# dropdown.select_by_value("option_value")
#
# # Pause to see the result (optional)
# time.sleep(5)

# Close the browser
# driver.quit()