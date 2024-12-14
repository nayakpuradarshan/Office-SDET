import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# initializing driver
service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# applied implicit wait for 10 seconds and maximize page
driver.implicitly_wait(10)
driver.maximize_window()

# get the mentioned url
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)

# Click on the mentioned link text
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)

# created variable and stored window handler to newly creted variable
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()

# Again came back to mentioned window page
driver.switch_to.window(windowsOpened[0])

# Verify that text is matching with mentined tag's text
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
time.sleep(5)

driver.close()
print("Success!")












