from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import  time

from selenium.webdriver.common import by
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

# Pause for 5 seconds to allow the page to load (optional)
time.sleep(3)

# Scroll down the page by 500 pixels using JavaScript
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
# Additional actions or verifications can be done here

# Close the browser
driver.quit()

# if driver is open:
#     print("working fine")
# else:print("errorrrr!!!!!!!!!!")