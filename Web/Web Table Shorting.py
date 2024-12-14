import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

service_obj = Service(executable_path="D:\Darshan\PERSONAL\Python Automation\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

All_veg = 0

Veg_WebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
print("Web Elements are: ", len(Veg_WebElements))

for veg_E in Veg_WebElements:
    All_Veg = veg_E.text

All_veg.sort()