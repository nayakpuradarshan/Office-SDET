import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

Buttons = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(Buttons))

for button in Buttons:
    if button.get_attribute("value") == "option2":
        button.click()

radios = driver.find_elements(By.XPATH, "//input[@type='radio']")

print(len(radios))

for radio in radios:
    if radio.get_attribute("value") == "radio3":
        radio.click()

driver.find_element(By.ID,"alertbtn").click()

alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
alert.accept()          # To accept alert
alert.dismiss()         # To cancel alert

time.sleep(3)
print('success')


