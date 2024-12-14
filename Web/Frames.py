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

driver.get("https://the-internet.herokuapp.com/iframe")

wait = WebDriverWait(driver, 20)

driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.TAG_NAME, "p").clear()
# driver.find_element(By.TAG_NAME, "p").send_keys("Automation is soo simple you know!")
time.sleep(4)

driver.close()
print("Success!")

