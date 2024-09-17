from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.support import  expected_conditions

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Specify the path to the chromedriver executable
service = Service(executable_path=r"C:\Users\archi\Downloads\chromedriver-win32\chromedriver.exe")

# Initialize the WebDriver with service and options
driver = webdriver.Chrome(service=service, options=options)

# Navigate to a URL
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)

# Locate an element (WebDriver will wait up to 10 seconds before throwing an exception)
element = (driver.find_element(By.ID, "alertbtn"))
# Perform actions on the element
# element.click()

# Close the WebDriver
driver.quit()

# element = WebDriverWait(driver, 10).until(
#     EC.elements_to_be_clickable((By.ID, "alertbtn"))
# )