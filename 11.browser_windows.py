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
driver.get("https://demo.automationtesting.in/Windows.html")

# how handle window
#
# current_window_handle - parent
#
# window handles - child

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()
print(driver.current_window_handle)



# window handles

handle = driver.window_handles
for handle in handle:
    driver.switch_to.window(handle)
    print(driver.title)

    if driver.title == "Frames and windows":
        driver.close()
        print(driver.title)