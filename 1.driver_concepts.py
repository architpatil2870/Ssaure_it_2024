from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path=r"C:\Users\archi\Downloads\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# webdriver commands
print(driver.title)
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
driver.implicitly_wait(10)
# driver.quit()