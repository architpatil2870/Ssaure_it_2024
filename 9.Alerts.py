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


trigger_button = driver.find_element(By.ID, "alertbtn")
trigger_button.click()

# Switch to the alert
alert = driver.switch_to.alert

# Print the alert text
print(alert.text)

# Accept the alert
alert.accept()
time.sleep(3)

print(driver.title)
# Close the browser
#driver.quit()