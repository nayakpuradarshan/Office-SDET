import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# initializing driver
service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# applied implicit wait for 10 seconds and maximize page
driver.implicitly_wait(10)
driver.maximize_window()

# get the mentioned url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(4)

# Go to the mentioned xpath
action = ActionChains(driver)
action.move_to_element(driver.
                       find_element(By.XPATH, "//div[@class='mouse-hover']")).perform()
time.sleep(3)

# # click on the mentioned link text
action.context_click(
    driver.find_element(By.LINK_TEXT, "Top")).perform()
time.sleep(3)

# click on the reload button
action.move_to_element(
    driver.find_element(By.LINK_TEXT, "Reload")).perform()
time.sleep(3)

print("Code performed successfully!")