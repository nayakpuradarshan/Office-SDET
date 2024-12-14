import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome browser invocation
service_obj = Service("D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("darshanisheretostay")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
time.sleep(5)

driver.find_element(By.XPATH, '//input[@type="submit"]').click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "successfully" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Darshan is here to stay")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(5)
print("success!")

driver.close()