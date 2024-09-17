from selenium.webdriver import  ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Specify the path to the chromedriver executable
service = Service(executable_path=r"C:\Users\archi\Downloads\chromedriver-win32\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
# method availble in chrome class
driver.get("https://rahulshettyacademy.com/AutomationPractice/")



# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Locate the web table using xpath
table = driver.find_element(By.XPATH, "//table[@name='courses']")

# Find all rows in the table, excluding the header row
rows = table.find_elements(By.XPATH, "tr")[1:]

# Loop through each row and print the course name and price
for row in rows:
    # Find all columns in the row
    cols = row.find_elements_by_tag_name("td")

    # Extract and print course name (1st column) and price (3rd column)
    course_name = cols[0].text
    course_price = cols[2].text
    print(f"Course Name: {course_name}, Price: {course_price}")

# Close the browser
driver.quit()
