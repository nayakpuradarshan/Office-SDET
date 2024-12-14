from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# created driver object
service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Maximize window wih implicit wait
driver.implicitly_wait(10)
driver.maximize_window()

# get mentioned url
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

# Get screenshot
# driver.save_screenshot("homepage.png")

# Using below mentioned line you can get source code of the webpage
# source = driver.page_source
# print(source)

# driver.find_element(By.LINK_TEXT, "Challenging DOM").click()
# time.sleep(4)
#
# # wait = webdriverWait(driver, 10)
#
# # Close driver
# driver.close()
#
# # Print below message
# print("Finally you're successsful!")

