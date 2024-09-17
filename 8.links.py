from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import  time
from selenium.webdriver.common.by import By

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

# Link concept
# Tag_name
# Link_text
# Partial_link_text

links = driver.find_elements(By.TAG_NAME, "a")

# print(len(vars()))

# for getting text
# for links in links:
#     print(links.text)


# how to clcik on link

driver.find_element(By.LINK_TEXT, 'Home').click()
print("done working.........")
