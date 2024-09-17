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

driver = webdriver.Chrome()

# Find the file input and upload a file
file_input = driver.find_element(By.NAME,'file_upload')
file_input.send_keys('/path/to/your/file.txt')
