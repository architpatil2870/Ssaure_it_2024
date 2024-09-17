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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


options = Options()
options.headless = True  # Run in headless mode

driver = webdriver.Chrome(options=options)
driver.get('https://example.com')
print(driver.title)  # Runs in the background
