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

driver.find_element(By.XPATH, "//a[@id='opentab']").click()
tab = driver.window_handles[1]
driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
window2 = driver.window_handles[2]
driver.switch_to(tab)
# how to handle multi window
print(driver.window_handles)
driver.find_element(By.XPATH, "//a[normalize-space()='Access all our Courses']").click()
driver.switch_to(window2)



# using this we hand multi window
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH, "//a[normalize-space()='Access all our Courses']").click()
#
