from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Specify the path to the chromedriver executable
service = Service(executable_path=r"C:\Users\archi\Downloads\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
# Add a cookie
driver.add_cookie({'name': 'test_cookie', 'value': 'test_value'})
# Get all cookies
cookies = driver.get_cookies()
print(cookies)
# Delete a specific cookie
driver.delete_cookie('test_cookie')
