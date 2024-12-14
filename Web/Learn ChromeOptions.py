from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
options = Options()
options.add_argument('--headless')  # Run in headless mode
# options.add_argument('--disable-gpu')  # Disable GPU acceleration
# options.add_argument('--window-size=1920,1080')  # Set window size (optional)
# options.add_argument('--no-sandbox')  # Bypass OS security model
# options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

# Specify the path to the ChromeDriver
service_obj = Service(executable_path="D:/Darshan/PERSONAL/Python Automation/chromedriver-win64/chromedriver.exe")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service_obj, options=options)

# Example: Open a webpage and print the title
driver.get('https://www.example.com')
print(driver.title)

# Quit the driver
driver.quit()
