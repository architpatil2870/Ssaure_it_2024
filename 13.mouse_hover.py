from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import  time
from selenium.webdriver import  ActionChains
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
driver.maximize_window()

# Navigate to a URL
driver.get("https://automationtesting.in/trainings/")

action = ActionChains(driver)
menu = driver.find_element(By.XPATH, "//a[normalize-space()='Reports']")
action.move_to_element(menu).perform()
submenu = driver.find_element(By.XPATH, "//a[normalize-space()='Extent Reports']']")
submenu.click()

time.sleep(3)