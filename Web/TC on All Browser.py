
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome browser invocation
service_obj = Service("D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
# Firefox browser invocation
# driver = webdriver.Firefox()

# Edge browser invocation
# driver = webdriver.Firefox()

driver.get("https://www.ajio.com")

print(driver.title)
print(driver.current_url)

