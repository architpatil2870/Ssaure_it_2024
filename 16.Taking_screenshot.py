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

# method 1

driver.get_screenshot_as_file('screenshot.png')

# Close the browser
driver.quit()


# try:
#     driver.get('https://rahulshettyacademy.com/AutomationPractice/')
#     assert "Example Domain" in driver.title
# except AssertionError:
#     driver.save_screenshot('test_failure.png')  # Captures screenshot
# finally:
#     driver.quit()
