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
driver.get("https://sso.teachable.com/secure/9521/identity/sign_up/email")

# input/text box
# user_name
driver.find_element(By.ID, "user_name").send_keys("archit")
driver.find_element(By.ID, "user_email").send_keys("archit8545@gmail.com")
driver.find_element(By.ID, "password").send_keys("archit234")


driver.find_element(By.NAME, "commit").click()

time.sleep(5)
print("all is done working")
