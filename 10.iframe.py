from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
# courses-iframe

driver.switch_to.frame("iframe-name")
(driver.find_element(By.XPATH, "//div[@class='nav-outer clearfix']//a[normalize-space()='Courses']")).click()

driver.switch_to.default_content()

(driver.find_element(By.CLASS_NAME, "dropdown-toggle")).click()

